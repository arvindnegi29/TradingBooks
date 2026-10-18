# Chart identification, scanning and annotation workflow

## Scope and retrieval
Read [Bulkowski complete review](book-notes/bulkowski-chart-patterns-full.md) and relevant chapter notes before attributing a rule. This workflow combines source-supported concepts with explicitly identified local presentation/research conventions. The original book describes visual systems, not a complete mechanical scanner. The geometry helper performs supplied-anchor arithmetic only; it detects no pattern, retrieves no market data and places no orders.

Read [pattern-coverage.json](pattern-coverage.json) for core-family coverage and implementation status. Read the appendix inventory in [PDF301–344 notes](book-notes/bulkowski-pdf301-344.md) for EVERY glossary silhouette; glossary-only names have no complete operational rule supplied. Use the [original schematic reference](../assets/chart-pattern-reference.svg) as geometry teaching aid, not source screenshots or detector output. Actual original exhibits can be opened at their cited PDFpages when source is available. Do not claim unseen original pictures were retrieved from bundled notes.

## 1. Establish observations before drawing
Resolve exact instrument/venue/timeframe/session/timezone, data window, bar-close convention, tick, currency, adjustment basis and log/linear scale. Use underlying/futures volume only where meaningful and available; index spot volume is not executable derivative volume. Keep incomplete bars separate. For screenshots alone, state visible limits and approximate coordinates; never invent exact prices/times from unreadable pixels.

First inspect the bare chart: incoming trend, meaningful swings, congestion and nearest obstacles. Then outline candidate geometry. Do not force patterns onto all price action or require a unique label. A rectangle can overlap a triangle, or a double bottom can become part of a larger formation. Evaluate independent evidence rather than label count. The user's requested dotted boxes may show congestion/level zones; they do not imply buy/sell orders.

## 2. Keep a finite scan ledger
For each requested family and timeframe record one of: unavailable_data, not_implemented, visually_assessed_no_match, developing, confirmed, invalidated_before_confirmation, adverse_break, strict_bust, ambiguous. Only use visually_assessed when an actual chart was examined; only claim computed_scan when a documented detector ran on actual data. A registry entry or book chapter is not a completed scan. Report requested-but-unassessed items explicitly.

Select and disclose pivot widths, tie rule, price similarity/touch tolerance, minimum separation, allowed boundary violations, duration, occupancy/traversal criterion, inbound-trend rule, volume comparison and close/buffer convention before a repeatable scan. Bulkowski's approximate5day swing rule has explicit visual exceptions. Numerical intraday adaptations are local research rules, not the book's empirically validated parameters. A five-right-bar pivot cannot be used until the fifth right bar closes. Freeze each parameter/boundary version at decision time.

## 3. Create objects with causal provenance
For every retained object record:
- id; family/subtype; market/contract/timeframe; source chapter/PDF/exhibit; assessment_method(visual/computed); parameter_version.
- Each anchor's bar time/index, observed price, pivot kind and known-at time; scale; line equation or low/high zone bounds; valid-from/last-updated time.
- Incoming trend and independent context; alternative plausible geometry; completed confirmation time/price; preconfirmation invalidation.
- Actual original breakout boundary versus whole-pattern extrema; excursion denominator; adverse-cross time; strict-bust time and count_so_far.
- Projection type/anchors/raw price; tick-valid order scenario separately; planned stop, entry assumption, costs, net RR, cancellation and stale-data state.

Do not reuse exhibit letters as global identifiers: source letters can repeat even within a chart. Use semantic names such as head_low,neckline_at_head,right_armpit_high,first_confirming_close,whole_pattern_low. Never silently edit historical anchors to fit later outcomes.

## 4. Pattern-specific marking and confirmation
|Family|Required anchor geometry|Confirmation reference and key caveat|
|---|---|---|
|Rectangle top/bottom|Near-horizontal repeated highs/lows,2distinct swings each minimum,3preferred; inbound trend names top/bottom|Close outside selected side; either exit direction. Genuine swing contacts and interior occupancy matter; event-driven flatline needs separate context.|
|Ascending triangle|Near-horizontal highs plus rising lows; repeated interior traversals|Close beyond actual boundary; either direction. Mark apex as time projection, not price target.|
|Descending triangle|Falling highs plus near-horizontal lows|Close beyond actual boundary; either direction. Four total contacts minimum,5preferred; no whitespace-only mountain enclosed by lines.|
|Symmetrical triangle|Falling highs/rising lows converging;2contacts each minimum,3preferred|Close outside; no shape-only directional certainty. Breakout70–75%toward apex is time location, not trade probability.|
|Flag / pennant|Separate strong pole from short/proportionate consolidation; flag parallel, pennant converging|Record actual side and trigger. Can reverse; touch counts differ from triangles. Typical3week daily limit has source exceptions, not an intraday constant.|
|Double bottom|Two lows plus maximum intervening high, downtrend role for reversal|Close above intervening high; below lowest low first invalidates. Candidate vs confirmed; Adam/Eve label first then second left-to-right.|
|Triple bottom|Three near-level lows, both internal peaks|Close above higher internal peak; below lowest low first invalidates. Distinct deeper middle may be H&S.|
|Double top|Two highs plus minimum intervening valley, uptrend role for reversal|Close below intervening low; above highest high first invalidates. A later third peak cannot revoke earlier confirmation.|
|Triple top|Three near-level highs, both internal valleys|Close below lower internal valley; distinguish fourth peak before versus after confirmation.|
|H&S bottom|LS/head/RS lows,head deepest; armpit highs; symmetry qualitative|Close above neckline; if neckline rises,use horizontal RIGHT-armpit HIGH instead. Upward approach may be continuation morphology,not reversal.|
|H&S top|LS/head/RS highs,head highest; armpit lows|Close below neckline; if neckline falls,use horizontal RIGHT-armpit LOW instead. Mere touch/pierce insufficient.|

Keep morphology, trend role, confirmation and profitability separate. Pattern-state invalidation is not automatically an executable stop recommendation. Source buy-stop intrabar entries and close-confirmed variants are different policies: specify the chosen one and never fill before confirmation if that policy requires a close. Avoid conflict with Volman's distinct intrabar-after-completed-signal model.

## 5. Distinguish returns, failures and busts
Bulkowski throwback follows upward breakout; pullback follows downward breakout. Both require departure, a genuine loop and return within30calendar days in the original definition. This is not the generic term pullback in other books; do not impose the30day rule on their methods or turn it into30five-minute bars. Retest itself is not a failed breakout.

Strict bust requires original confirmed breakout, insufficient excursion in that direction, then a CLOSE beyond opposite WHOLE-pattern extreme. General source uses about10%, with inconsistent strict/equality wording; one page says1%. Preserve ambiguity, declare any exact implementation and reference price. A crossing of a sloped line/right shoulder can be an adverse-break warning while still far from full bust. Track single/double/triple count_so_far, never future eventual-single status. No-throwback, ultimate high/low and final pattern duration are retrospective until observed under an explicit rule.

## 6. Calculate levels from prices, not screen distances
|Projection|Correct price arithmetic|Notes|
|---|---|---|
|General height|H=pattern_high−pattern_low;target=breakout±H|For sloped boundaries,breakout is actual line value there,not necessarily an extreme.|
|H&S|H=abs(head−neckline_at_head_time);target=actual_breakout±H|Do not substitute full bounding box or neckline value at a different date for height.|
|Flag/pennant up|prebreakout-day_low+(pole_high−pole_low)|SourceCh21; resistance can justify nearer scenario. Downward mirror is a disclosed geometric adaptation,not independently tested source strategy.|
|Swing up|2*old_peak−retracement_low|Project above old peak,not from retracement low.|
|Swing down|2*old_trough−rally_high|Project below old trough,not from rally high.|
|Continuation gap|2*gap_midpoint−trend_start|Requires separately justified provisional/confirmed gap classification.|
|Triangle apex|IntersectionTIME of selected lines|A nearby minor high OR low is hypothesized; no automatic bearish signal or apex-price target.|

Fractional-height targets produced by multiplying H by historical hit-rate percentages are author's nearer-target heuristics; they do not create corresponding new success probabilities. Actual targets should face current obstacles, costs and trade horizon. Never recommend a nonpositive underlying-price target as executable merely because arithmetic produced it.

Optional helper: python scripts/chart_geometry.py request.json. Projection example:
```json
{"operation":"projection","kind":"head_shoulders","direction":"down","head":17,"neckline_at_head":14.47,"breakout":15.05}
```
Returns12.52,not a trade signal. For line evaluation pass operation=line,anchors=[{bar,price,known_at_bar},{bar,price,known_at_bar}],at_bar,asof_bar,scale=linear/log. It rejects future-unavailable anchors; marks historical reconstruction as retrospective_line_value and extension beyond asof as future_projection. Fractional bar indices are just numeric coordinates, not calendar dates. Use equally spaced bar indices for the actual plotted series; elapsed-time coordinates are a different declared model. Helper cannot verify supplied anchors, source event times, pivot validity, tick/lot/currency or chart classification. Its arithmetic tests are not strategy validation.

## 7. Draw readable, honest chart overlays
Local presentation convention, not author-mandated colors:
- Thin neutral solid lines for observed boundaries; dotted outlines/translucent boxes for candidate zones; clearly labeled dashed projections in unused future area. A rightward extension is a scenario, not future data.
- Put compact labels outside candle bodies, with leader lines where needed. Include timeframe,family,state and keyprice; move labels to separate rows instead of overlapping. Keep price/volume panels distinct.
- Label LS/Head/RS or P1/P2/P3,L1/L2/L3 only on correct swings. Add neckline/confirmation,first closing trigger and whole-pattern invalidation as different objects.
- Use muted labels for invalidated history and show invalidated-at time. Never erase a bad candidate to make the historical chart look perfect. Declutter to nearest relevant context and bestsupported candidates; detailed ledger carries the rest.
- Keep price target,apex-date alert,underlying invalidation,option-premium stop and assumed execution price visibly distinct. Avoid multiple arrows suggesting certain future direction. State approximate screenshot-derived coordinates.

Where an authorized chart drawing interface is available, apply these actual objects and verify the result visually after editing. If unavailable, provide coordinates/annotation plan or a clearly labeled reconstructed chart; never claim the user's chart or Pine indicator was edited. Skill upgrade does not install a TradingView drawing integration or change other plugins.

## 8. Preserve research and trading boundaries
All source equity statistics retain market regime,sample,period,definition and hindsight limitations. Perfect-trade ultimate-high returns, target attainment, direction frequency and net profitable trades are different outcomes. Do not transfer USdaily percentages, pennies, duration or liquidity rules to BTC/India as calibrated parameters. No book majority vote or correlated-label confidence score. Preserve exact option quote/IV/Greeks/lot checks,user cash risk,provider recovery,manual execution and existing failed BTC-model diagnostic. Do not copy source no-stop examples or fixed whole-pattern stops that exceed budget. No live chart scan or trading strategy validation is implied by this workflow release.
