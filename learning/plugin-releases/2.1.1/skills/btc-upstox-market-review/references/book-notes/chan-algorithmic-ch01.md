# Algorithmic Trading: Chapter 1 checkpoint

Ernest P. Chan, Algorithmic Trading: Winning Strategies and Their Rationale (2013).
File: New Folder/Algorithmic Trading - Winning Strategies and Their Rationale 2013 - annotated.pdf
Blob: b989ccdd650e8f1ff6b30f6c7164410c8ba7622a
Source: https://github.com/arvindnegi29/TradingBooks/blob/284a6c51261a6d7fb7499f4eb00ca20c60d554fa/New%20Folder/Algorithmic%20Trading%20-%20Winning%20Strategies%20and%20Their%20Rationale%202013%20-%20annotated.pdf
225 PDF pages. Read: preface (11-17) and Chapter 1 (19-56).
Visual checks: PDF pages 35, 45, 49. Other annotations not exhaustively inspected.
Code examples read, not executed or validated. Next: Chapter 2, PDF page 57.

## Source summary and citation map
- Preface, PDF 15-16: example strategies are prototypes; costs and optimization choices limit performance claims.
- Chapter 1, PDF 20-25: independently reproduce implementations, avoid look-ahead and data snooping, and protect later-period tests from repeated tuning.
- PDF 26-34: data adjustments, survivorship, venue alignment, contract stitching and asynchronous prices can distort results.
- PDF 34-40: significance depends on the null model; p-values are not probabilities that a strategy will win.
- PDF 40-43: benchmarks and regime changes matter.
- PDF 43-56: platform/data/execution consistency matters; historical product comparisons are not current recommendations.

## Integration safeguards
Methodology reference only. It supplies no current BTC entry level.
Keep the existing no-look-ahead, venue-specific execution and independent validation gates. Never relabel the plugin's failed later-period models as validated.
A shared backtest/live codebase alone does not guarantee freedom from leakage: inspect upstream features, timestamps and data availability too.
No trading automation or execution authorization is added.
