# Volume Price Analysis: first reading checkpoint

Author: Anna Coulling. Edition: 2013.
Source: https://github.com/arvindnegi29/TradingBooks/blob/284a6c51261a6d7fb7499f4eb00ca20c60d554fa/A%20Complete%20Guide%20To%20Volume%20Price%20Analysis%202013.pdf
Source blob: b4c9ef63534338049ffdb5e2ddbc267b88281d70
PDF length: 157 pages.
Reviewed: title/disclaimer/contents, foreword and Chapter One, PDF pages 9-17.
Next: Chapter Two starts at PDF page 18. Not yet reviewed.
Status: PARTIAL. No whole-book completion claimed.

## Concise source summary
Chapter One traces price-volume interpretation through Dow, Wyckoff, Livermore and ticker-tape practice. It presents supply/demand, cause/effect and effort/result as interpretive principles. Its practical emphasis is to compare price movement with trading activity, time and trend context. The author makes strong claims about broad applicability and identifying professional activity; these are author assertions, not independently established findings from this reading. Sources: PDF pages 9-17; especially 10-11 and 15-17.

## Critical assessment
The reviewed introduction supplies no reproducible BTC perpetual backtest. Historical anecdotes and forecasts are not validation. Do not adopt claims of certainty or universal manipulation as established facts. Treat the framework as a source of hypotheses.

## Proposed implementation work, not rules taken verbatim from the book
- Compare the same venue, contract and volume unit across completed candles.
- Define relative volume using prior bars only; choose and freeze the baseline before testing.
- Describe large volume with little price progress as an anomaly needing confirmation, not proof of accumulation.
- Require subsequent observable price acceptance/rejection and structural invalidation.
- Keep candle-based observations separate from trade-level aggressor flow, order-book evidence and OI changes.
- Test costs, funding, slippage and different volatility/session regimes.
No thresholds have been selected, no detector implemented and no edge validated.

## Learner drill proposal
Use simulated BTC candles. Present a move into a prior high with rising activity and limited upward progress. Ask the learner to give two competing explanations, a confirmation trigger, invalidation and a WAIT condition. Keep the outcome hidden until the answer. Label the example simulated.

## Plugin status
Reference notes only. The installed BTC & Indian Market Review plugin has not been modified or fine-tuned.
