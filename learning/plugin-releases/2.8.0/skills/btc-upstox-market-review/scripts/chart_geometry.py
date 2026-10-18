"""Numerical marking helpers, not chart-pattern detectors or trade signals.

CLI: python chart_geometry.py request.json
Input has operation=line or projection. See chart-pattern-workflow.md.
Only supplied anchors are used. No market access, orders or historical testing.
"""
import json
import math
import sys


def number(value):
    if isinstance(value, bool):
        raise ValueError('Boolean is not a price or bar coordinate')
    value = float(value)
    if not math.isfinite(value):
        raise ValueError('Finite numeric inputs required')
    return value


def line_value(anchors, at_bar, asof_bar, scale):
    if len(anchors) != 2 or scale not in ('linear', 'log'):
        raise ValueError('Two anchors and explicit linear/log scale required')
    a, b = anchors
    x1, x2 = number(a['bar']), number(b['bar'])
    y1, y2 = number(a['price']), number(b['price'])
    at_bar, asof_bar = number(at_bar), number(asof_bar)
    if x2 <= x1:
        raise ValueError('Anchor bars must increase')
    for anchor in anchors:
        known = number(anchor['known_at_bar'])
        if known < number(anchor['bar']) or known > asof_bar:
            raise ValueError('Anchor not causally available at as-of bar')
    fraction = (at_bar - x1) / (x2 - x1)
    if scale == 'log':
        if min(y1, y2) <= 0:
            raise ValueError('Log-price anchors must be positive')
        result = math.exp(math.log(y1) + fraction * (math.log(y2) - math.log(y1)))
    else:
        result = y1 + fraction * (y2 - y1)
    known_at = max(number(anchor['known_at_bar']) for anchor in anchors)
    status = ('future_projection' if at_bar > asof_bar else
              'retrospective_line_value' if at_bar < known_at else 'line_value')
    return {'price': number(result), 'scale': scale,
            'status': status, 'anchors_known_at_bar': known_at,
            'causal_at_evaluation_bar': known_at <= at_bar,
            'at_bar': at_bar, 'asof_bar': asof_bar}


def projection(kind, direction, **values):
    if direction not in ('up', 'down'):
        raise ValueError('Explicit up/down direction required')
    v = {k: number(x) for k, x in values.items()}
    sign = 1 if direction == 'up' else -1
    if kind == 'height':
        height = v['high'] - v['low']
        base = v['breakout']
        formula = 'breakout +/- (high-low)'
    elif kind == 'head_shoulders':
        height = sign * (v['neckline_at_head'] - v['head'])
        base = v['breakout']
        formula = 'breakout +/- abs(head-neckline_at_head)'
    elif kind == 'flag':
        height = sign * (v['pole_end'] - v['pole_start'])
        base = v['prebreak_extreme']
        formula = 'prebreak_extreme +/- abs(pole_end-pole_start)'
    elif kind == 'swing':
        height = sign * (v['old_extreme'] - v['retracement_extreme'])
        base = v['old_extreme']
        formula = '2*old_extreme-retracement_extreme'
    elif kind == 'continuation_gap':
        height = sign * (v['gap_midpoint'] - v['trend_start'])
        base = v['gap_midpoint']
        formula = '2*gap_midpoint-trend_start'
    else:
        raise ValueError('Unsupported projection kind')
    if height <= 0:
        raise ValueError('Anchor ordering contradicts direction or has zero height')
    return {'target': number(base + sign * height), 'height': height,
            'kind': kind, 'direction': direction, 'formula': formula,
            'status': 'projection_only',
            'warning': 'Not a signal, fill, probability or validated price forecast; verify anchors and tick/cost constraints'}


def run(request):
    request = dict(request)
    operation = request.pop('operation')
    if operation == 'line':
        return line_value(**request)
    if operation == 'projection':
        return projection(**request)
    raise ValueError('Unsupported operation')


if __name__ == '__main__':
    try:
        with open(sys.argv[1], encoding='utf-8') as source:
            result = run(json.load(source))
        print(json.dumps(result, indent=2, allow_nan=False))
    except (ValueError, KeyError, TypeError, IndexError, OSError, OverflowError) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        sys.exit(2)
