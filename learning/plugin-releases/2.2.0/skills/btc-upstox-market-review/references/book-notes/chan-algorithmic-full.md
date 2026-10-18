# Chan 2013: complete-text review and operational adaptation

## Identity, coverage and limits
Ernest P. Chan, Algorithmic Trading: Winning Strategies and Their Rationale, Wiley, 2013.
Uploaded file: Algorithmic Trading - Winning Strategies and Their Rationale 2013 - annotated.pdf.
SHA-256: 1c8b27ebee9f35f964794013e8629e5343c23506fa890ad65783867e8b3518ba.
225 PDF pages. The upload is byte-identical to the earlier New Folder copy, so the already-read Chapter 1 was reused after hash verification. All remaining chapter text, examples, conclusion, bibliography, author/website pages and index were read in this session. Blank pages are included in coverage, not counted as substantive material.
Repository source blob: b989ccdd650e8f1ff6b30f6c7164410c8ba7622a.
Immutable repository reference: https://github.com/arvindnegi29/TradingBooks/blob/284a6c51261a6d7fb7499f4eb00ca20c60d554fa/New%20Folder/Algorithmic%20Trading%20-%20Winning%20Strategies%20and%20Their%20Rationale%202013%20-%20annotated.pdf

Status: COMPLETE TEXT REVIEW; selected visual inspection; NOT empirical strategy replication.
The file contains zero embedded PDF annotation objects, despite its filename. This does not exclude marks flattened into page images. No claim of having independently proved every equation or reproduced every reported return is made.
The examples are historical research prototypes. No returns, Sharpe ratios, p-values or optimal leverages in this book are current BTC or Indian-options estimates.

## Chapter and page map
PDF page = printed Arabic page + 18 for Chapters 1-8 and conclusion.
| Section | PDF pages | Main subjects |
|---|---|---|
| Front matter/preface | 1-18 | Scope, prototype limitations, costs and hindsight caveats |
| 1 | 19-56 | Backtest errors, significance, data/execution consistency |
| 2 | 57-80 | ADF, Hurst/variance ratio, half-life, cointegration, linear portfolios |
| 3 | 81-104 | Price/log/ratio spreads, Bollinger entries, scaling, Kalman, bad ticks |
| 4 | 105-124 | Equity/ETF pairs, intraday gap reversal, basket-relative strategies |
| 5 | 125-150 | Currency units/carry, futures curve/roll, calendar/intermarket spreads |
| 6 | 151-172 | Horizon-specific momentum, carry, relative ranking, news/forced flows |
| 7 | 173-186 | Intraday breakouts, events, rebalancing, depth and signed trades |
| 8 | 187-204 | Leverage, growth, drawdown, CPPI, stops, strategy-specific risk indicators |
| Conclusion | 205-208 | Mechanism first, unseen-data tests and continuing regime judgment |
| Back matter | 209-225 | Bibliography, author, website and index; cited works not independently read |

## Research lessons, with exact references
1. Implementation details are part of the hypothesis, not afterthoughts (Ch1, PDF 20-34). Preserve instrument/venue, timestamp, price type, execution timing and all costs.
2. Repeatedly tuning a failed holdout contaminates it (Ch1, PDF 21-25). Keep the plugin's existing failed later-period results intact; use new independent data after a frozen revision.
3. Statistical evidence depends on test specification and benchmark (Ch1, PDF 34-42). A p-value is not the posterior probability of a hypothesis or a trade success rate.
4. Mean reversion must be distinguished from an expectation based only on a visual deviation (Ch2, PDF 57-68). A short estimated half-life is not proof of net profitability.
5. Correlation is not cointegration. Estimated spread coefficients and tests must be fitted on training data with appropriate residual-test critical values (Ch2, PDF 68-78).
6. Price spreads, log spreads and ratios imply different exposure/rebalancing assumptions (Ch3, PDF 82-88). Raw regression coefficients cannot silently become contract quantities.
7. Dynamic estimation can adapt but adds assumptions and free parameters (Ch3, PDF 92-101). Keep Kalman noise choices, initialization and causal timing explicit.
8. Tiny quote errors can produce large percentage spread errors (Ch3, PDF 101-103). Outlier correction cannot assume every sharp market move is erroneous.
9. Basket and session strategies need point-in-time constituents and feasible auction/open execution (Ch4, PDF 106-123). Selecting with an official open and filling at that same open is not automatically feasible.
10. Spot, futures curve returns and financing are different (Ch5, PDF 125-149). Historical dated-futures convergence models do not establish a perpetual funding strategy.
11. Mean reversion and momentum can coexist at different horizons (Ch6, PDF 152-159). Avoid using a generic Hurst estimate to overrule all timeframe evidence.
12. Flow/event explanations require matching observable data and announcement availability (Ch6-7, PDF 166-186). Candles cannot establish fund redemptions or informed institutional identity.
13. Growth optimization is sensitive to estimated means, tails and constraints (Ch8, PDF 188-198). Kelly is not an automatic retail sizing recommendation.
14. Stops, capital floors and diversification do not eliminate gap, liquidity or model risk (Ch8, PDF 198-204). Risk indicators must be evaluated for the actual strategy.

## Independent critical review: do not silently propagate these issues
These are review findings about this printed copy, not a claim that every publisher code download has the same issues.
- Example 7.1, PDF 174 / printed 156: the printed P&L expression has the opposite sign to the stated long-open/short-open momentum positions. A long from 100 to 110 must profit before costs; the printed expression produces a loss. Flag and independently verify a corrected implementation before any replication.
- Example 2.7, PDF 75 / printed 57: the statement that both Johansen tests establish all three relations conflicts with the displayed maximum-eigenvalue first-row statistic versus its 95% critical value. Apply the sequential rank test instead of accepting the prose.
- Example 3.3, PDF 96-97: the displayed initial loop references the prediction covariance before its first-iteration assignment. The source fragment is incomplete or inconsistent as printed; verify initialization from a tested implementation.
- Several statistical interpretations use certainty language too loosely, including PDF 64. Never report a p-value as the probability that a process is random or that a trade wins.
- Chapter 2's broad use of stationarity is a heuristic description. In implementation, distinguish weak/strict stationarity, finite-sample persistence, structural breaks and model assumptions. Do not label every Hurst estimate below 0.5 as proof of stationarity.
- PDF 193 shows a growth approximation whose variance term must be checked against the displayed constrained-growth expression and dimensions; do not code the printed scalar expression blindly.
- PDF 153-154's prose/code sampling descriptions differ; do not assume that either automatically eliminates all dependence between adjacent return-pair observations. Construct the intervals and inspect overlap; use appropriate dependence-aware inference.
- The PDF 199 CPPI example and surrounding claims require independent formula/path validation. PDF 200 itself acknowledges gap/suspension risk. Do not promise a guaranteed drawdown cap.
- Earlier historical U.S. rules, platform capabilities, fees, websites and market behavior are not current specifications. Verify changing facts from current official sources if a future task needs them.
- Descriptions of deceptive quoting are not strategies this plugin will recommend or execute. Use quote persistence/trade confirmation only for defensive data interpretation.

## Adaptation to Delta BTCUSD perpetual and Upstox
The following are implementation requirements chosen for this plugin; they are not new validated strategies from the book.
### Signal gate
A. Identify mechanism, contract and horizon. If regime or mechanism is ambiguous, show both continuation and reversion cases and the deciding observation.
B. Use fresh executable quotes and completed candles; retain existing freshness/invalidation gates.
C. State what was actually calculated. No ADF/Johansen/Kalman/variance-ratio/Hurst detection claim without computed results, parameters, sample boundaries and diagnostics.
D. Resolve sign, multiplier, base/quote/settlement currency and gross-versus-net exposure before deriving P&L or quantity.
E. Model fees, bid/ask, slippage, funding or financing at applicable event times. Delta perpetuals have no dated-contract expiry roll; Upstox futures/options require actual contract expiries and metadata.
F. Keep book hypotheses experimental until implemented and evaluated on unseen chronological data. No FVG, OB, CHOCH or MSS provenance is supplied by this book merely because breakout behavior is discussed.
G. Require user cash-risk limits, a bounded stop/invalidation plan and exchange lot increments. Do not default to Kelly, unbounded scaling, removing stops or account/position access.
H. For options, a directional underlying hypothesis does not determine premium P&L; retain actual bid/ask, expiry, IV/Greeks and premium-risk requirements.

### Required reference output
Use: Chan (2013), chapter, printed page and 1-based PDF page, specific concept, current evidence, contrary interpretation, implementation/validation status.
Example: "Ch7, printed 167-168 / PDF 185-186: signed transaction flow; unavailable because only candle/depth snapshots were supplied." Do not present unavailable flow as positive confirmation.
A book reference is conceptual provenance, not a probability estimate or a signal vote.

## What changed and what did not
Added reasoning, source/citation coverage, model-risk checks and source-code caution.
No new signal detector, broker API, order execution, historical options endpoint, measured win rate or validated trading edge was implemented.
The six existing experimental BTC models' later-period failures remain binding.
