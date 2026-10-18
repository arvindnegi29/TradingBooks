# Curtis M. Faith, *Way of the Turtle* — full-book review

## Source and review coverage

Source: *Way of the Turtle: The Secret Methods that Turned Ordinary People into Legendary Traders* (Curtis M. Faith, 2007), uploaded PDF, 313 physical pages. The source is byte-identical to archive catalog item B144 (Git blob `af97477627b29b6a11430e28310e68ddccfd2f79`; SHA-256 `be5aa72d6a2204560cedf4db44dc061e14bdafaa9b6ad04b90c8b28ae23faf84`; 2,814,818 bytes). All physical pages 1–313 were text-reviewed page by page. The illustrated cover and substantive formula/table/price-ladder exhibits were visually checked; this is not an exhaustive full-resolution audit of every page. No strategy was backtested or replicated.

The six detailed reading notes contain page-level coverage, chapter summaries, source caveats and selected exhibit checks: [PDF 1–52](pages-001-052.md), [53–104](pages-053-104.md), [105–156](pages-105-156.md), [157–208](pages-157-208.md), [209–260](pages-209-260.md), [261–313](pages-261-313.md). References in this review use **physical PDF pages** unless labeled “printed.” Printed page numbering differs from PDF numbering.

## Book structure

| Physical PDF pages | Printed pages | Material |
|---|---:|---|
| 12–27 | xi–xxvi | Foreword, preface, introduction |
| 28–38 | 1–11 | 1. Risk Junkies |
| 40–54 | 13–27 | 2. Taming the Turtle Mind |
| 56–72 | 29–45 | 3. The First $2 Million Is the Toughest |
| 74–89 | 47–62 | 4. Think Like a Turtle |
| 90–100 | 63–73 | 5. Trading with an Edge |
| 102–111 | 75–84 | 6. Falling Off the Edge |
| 112–134 | 85–107 | 7. By What Measure? |
| 136–148 | 109–121 | 8. Risk and Money Management |
| 150–156 | 123–129 | 9. Turtle-Style Building Blocks |
| 158–176 | 131–149 | 10. Turtle-Style Trading: Step by Step |
| 178–204 | 151–177 | 11. Lies, Damn Lies, and Backtests |
| 206–233 | 179–206 | 12. On Solid Ground |
| 234–248 | 207–221 | 13. Bulletproof Systems |
| 250–260 | 223–233 | 14. Mastering Your Demons |
| 262–271 | 235–244 | Epilogue |
| 272–301 | 245–274 | Bonus: Original Turtle Trading Rules |
| 302–313 | 275–286 | Bibliography and index |

Blank physical pages are intentional. The bonus rules section is the book’s most precise description of the original system.

## Central lessons and evidence

Faith presents trading as a probabilistic business. A strategy must have positive expectancy over a series after costs; risk controls must allow the trader to survive losing runs; rules must be executed consistently; and a system should remain simple enough to capture its intended return distribution. The Turtle trend system deliberately accepted frequent small losses in pursuit of a few large winners. A single loss or winner does not measure the quality of a decision. These are process principles, not a claim that any particular present-day strategy has positive expectancy (PDF 56–66, 74–89, 90–100, 158–176).

The book reviews behavioral errors—loss aversion, sunk cost, disposition, outcome and recency bias, anchoring, herd behavior and overgeneralization from small samples (PDF 40–54). Its four descriptive market states are stable/quiet, stable/volatile, trending/quiet and trending/volatile; Faith says trend followers find quiet trends easier to hold (PDF 52–54). Neither the behavioral list nor regime descriptions provide calibrated detector thresholds or a validated live signal.

Faith argues that an edge must be evaluated through whole-system returns, costs, drawdowns, path dependence and robustness. The book distinguishes maximum favorable/adverse excursion (MFE/MAE), R-multiples, expectancy and volatility-normalized exposure, and discusses E-ratio as an entry diagnostic. Its reported E-ratio study uses 28 high-volume U.S. futures from 1996–2006 and author-selected filters; those historical values depend on sample, construction and horizon and are not current BTC or Indian-market probabilities (PDF 90–100). The later chapters discuss parameter sensitivity, bootstrap and out-of-sample evaluation, data-mining bias, robustness and the limits of backtests (PDF 178–248). Treat the metrics as candidates to calculate transparently, not standalone proof.

## Original Turtle mechanics (historical specification)

These mechanics describe the original futures rules as printed in the bonus appendix. The complete source examples and visually checked tables are in the 261–313 note.

- **Volatility:** `TR = max(H−L, |H−previous close|, |L−previous close|)`. The original smoothed volatility value is `N_t = (19*N_(t−1) + TR_t)/20`, seeded with the first 20-day simple average of TR. N is measured in price points (PDF 278–282).
- **Unit sizing:** one unit is `floor(0.01 × account equity / (N × dollars per point per contract))` whole contracts. Thus a 1N adverse move in one unit is intended to represent about 1% of equity, subject to rounding and actual fills. This was an account-specific historical convention, not a recommended risk setting (PDF 281–282).
- **Portfolio limits:** 4 units per market; 6 same-direction units in closely correlated markets; 10 in loosely correlated groups; 12 total in one direction. The group definitions and caps were historical. Faith recounts a 1987 rate-market episode with 40–60% one-day losses despite controls (PDF 283–285).
- **Entries:** System 1 buys/sells one tick beyond the prior 20-day high/low, skipping a signal if the prior breakout in that market would have been profitable under the rule; after a skipped winner, a 55-day failsafe breakout is taken. System 2 takes every 55-day breakout. The book’s earlier chapters call System 2 a 60-day breakout, while the original-rules appendix says 55 days (PDF 65–66; 88; 285–289). Preserve this discrepancy rather than choosing silently.
- **Pyramiding:** add one unit for each 0.5N move beyond the preceding actual fill, within portfolio caps (PDF 287–289).
- **Stops and exits:** standard protective stop 2N from entry, with earlier stops adjusted as units are added; an alternative 0.5N “Whipsaw” stop re-enters at the original level. System 1 exits on the opposite 10-day channel; System 2 uses the opposite 20-day channel (PDF 289–295). The Whipsaw advantage is asserted without a reproducible sample in this appendix.
- **Execution:** the book discusses order placement, liquidity, correlated signals, contract-month choice and futures rolls (PDF 296–301). Several recommendations reflect 1980s floor trading and are not direct instructions for current electronic venues.

## Source errors and unresolved arithmetic

Preserve rather than silently correct the printed source. Chapter 3’s example prints `$30 × 10 × 100 = $3,000`, though the stated multiplication is $30,000 unless the quote convention differs (PDF 63–64). Tables in Chapter 12 include values/changes that do not reconcile as printed: Table 12-1’s 4.9% RAR, Table 12-2’s 4% Donchian CAGR, and Table 12-4’s −5.0% R-cubed change for 7.68 to 3.94 (PDF 216–217, 225). In the appendix, the prose says a trade could not lose more than 2%, but applying the stated 1%-per-N unit size and the four crude-oil fills/stops in the printed example implies 5N (about 5% of sizing equity) before costs or gaps (PDF 290–293). The chapter flags tension between its fixed stops and earlier no-stop system discussion (PDF 290). N-based stops cannot bound losses through gaps or poor fills.

The foreword and introduction differ on the selection process and test-question counts; these may describe separate stages but are not reconciled (PDF 13–14, 21–22). Historical performance and Turtle-cohort anecdotes are the author’s and foreword’s claims, not independently audited evidence. Sample-dependent returns and market examples do not establish current expected returns.

## Application to BTCUSD and Indian markets

Use the book as a systems-design checklist: explicitly define the market universe, signal timing, volatility estimator, quantity rounding, adds, stops, exits, fees, funding, rolls, correlated exposure, gap/stress loss and behavior through drawdowns. For any calculation, use the actual current contract multiplier, tick value, venue, bar construction, lot size and user-authorized risk budget. Keep BTC spot, perpetual and futures data distinct; include funding, basis, liquidation, venue and continuous-session risks. For Indian instruments include current session, expiry, lot, margin, fee/tax and overnight-gap conditions.

Do not copy 1% per N, the 20/55/60-day parameters, half-N adds, 2N or 0.5N stops, 4/6/10/12 caps, 1980s execution tactics, or the historical performance claims into plugin defaults. Daily bar and gap definitions must fit the instrument and session. BTC is a single underlying, so related contracts are not automatically independent markets. Any adapted strategy requires point-in-time data, realistic costs/rolls/funding/slippage, out-of-sample and walk-forward tests, parameter sensitivity, drawdown and liquidation stress tests, and separate review before a performance claim. No book principle supplies fresh market data, implemented detection or permission to trade.

## Evidence limits

The source supports a detailed account of the author’s system and reasoning, with complete extracted-text coverage and selected visual checks. It does not provide a modern BTC/Indian-market test, verified current product specifications, an independently audited Turtle performance record, or a universally correct risk percentage. The review is not a formal verification of every equation/table and does not claim exhaustive full-resolution visual inspection.
