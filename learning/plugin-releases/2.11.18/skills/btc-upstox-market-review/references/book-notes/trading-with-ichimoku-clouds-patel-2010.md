# Manesh Patel — *Trading with Ichimoku Clouds* (2010)

## Source and review scope

- Source: user-uploaded PDF, *Trading with Ichimoku Clouds: The Essential Guide to Ichimoku Kinko Hyo Technical Analysis*.
- Author: Manesh Patel. Wiley's catalog identifies July 2010 and ISBN 978-0-470-60993-4. The scan's copyright page also says 2010; its OCR garbles the ISBN. Wiley lists 240 pages; this supplied scan has 237 physical PDF pages. Treat PDF page numbers and printed book folios as separate references.
- File identity: SHA-256 `0914cee8441ce2453019ba867a76d2550c4d93d8bdf1fb39e26484c406bbb0c7`; 10,881,845 bytes.
- Text coverage: all 237 physical pages reviewed in order, including front matter, all nine chapters, the analysis worksheet, bibliography, author page and index. The extracted scan has OCR errors and some equations/table symbols are degraded; check the page image before relying on an ambiguous symbol or number.
- Visual coverage: contact sheets screened all 237 pages. Higher-resolution inspection: PDF pp. 52, 55, 70, 87, 165, 173, 190, 214 and 224. This is not a pixel-level inspection of every individual chart.

## Chapter and page map

For the main numbered chapters, printed book page is generally physical PDF page minus 27 (for example, printed p. 25 is PDF p. 52). The front matter uses Roman numerals, so this offset does not apply there.

| Chapter / material | Printed pages | Physical PDF pages | Coverage |
|---|---:|---:|---|
| Introduction: background and components of a trading system | ix–xxvi | 10–27 | Ichimoku context, planning, objectives and system components |
| 1. Ichimoku Components | 1–40 | 28–67 | Five lines/cloud, trend context, visual examples and level interpretation |
| 2. Ichimoku Trading Plan | 41–44 | 68–71 | Historical daily FX plan and bullish/bearish rule tables |
| 3. Ichimoku Backtesting | 45–136 | 72–163 | EUR/USD walkthrough, Jan. 2007–Dec. 2008 in the actual narrative/results |
| 4. Post-Analysis | 137–148 | 164–175 | Outcome tables and proposed parameter changes |
| 5. Ichimoku Strategies | 149–160 | 176–187 | Foundation system and four additional strategy families |
| 6. Ichimoku Time Elements | 161–170 | 188–197 | Time-count hypothesis, chart procedure, Gann comparison |
| 7. Applied Trader Psychology (Doug Laughlin) | 171–180 | 198–207 | System fit, loss acceptance, conviction and journaling |
| 8. Day Trading with Ichimoku | 181–192 | 208–219 | Leverage/gap cautionary cases and a short 5-minute EUR/USD test |
| 9. Conclusion | 193–194 | 220–221 | Written trading plan, review and revision |
| Ichimoku Analysis Sheet | 195–197 | 222–224 | Checklist table for price/cloud, line relationships, Chikou and future cloud |
| Website/bibliography/author/index | 198–210 | 225–237 | Back matter; index and source list inventoried |

## Ichimoku components and the book's reading sequence

The standard formulas described by Patel are range midpoints, not simple moving averages of closes:

- **Tenkan-sen:** `(highest high + lowest low) / 2` over 9 bars. Shorter-term range midpoint.
- **Kijun-sen:** same midpoint over 26 bars. Medium-term reference in the book.
- **Chikou span:** current close plotted 26 bars back. Compare today's value with the actual price structure at that earlier time; it is a lagged display of current information.
- **Senkou Span A:** `(Tenkan + Kijun) / 2`, plotted 26 bars forward.
- **Senkou Span B:** 52-bar high/low midpoint, plotted 26 bars forward.
- **Kumo:** area between Span A and Span B. Keep the cloud at the current price location distinct from the cloud projected to the right of the current bar.

The book's context checklist reads the five components together:

1. Price above / inside / below the current cloud: bullish context / congestion / bearish context in the author's vocabulary.
2. Tenkan relative to Kijun, their slopes and whether either is flat. The book treats flat Tenkan/Kijun areas as possible consolidation and their range midpoints as dynamic references, not guaranteed barriers.
3. Chikou relative to the historical price and cloud. Patel calls it “open space” when the shifted line has room before it meets prior price. He asks the reader to test horizontal and vertical collision scenarios, including a 5–10-bar window. The chart is a visual check, not a measurable probability by itself.
4. Future Span A versus B, their slopes, and cloud thickness. The book reads order/direction as a future bias and thickness as evidence of prior congestion/volatility. These are contextual descriptions, not independent confirmations.
5. The prior cloud (“Kumo shadow”), flat Span B shelves, and Span A peaks as candidate support/resistance. In the example on printed p. 25 / PDF p. 52, a horizontal level is drawn through five Chikou peaks; Patel notes that a 23.6% retracement coincides with that level. This is an example of annotation, not proof that the level or Fibonacci overlap predicts a reversal.

The charts show a useful marking discipline: label the instrument and timeframe; keep current cloud and future cloud visually separate; mark a horizontal shelf or zone only where a specific prior cloud plateau, Chikou swing/peak, prior price pivot or chart level supports it; preserve the level's timeframe and source; then label alert, entry trigger, invalidation/stop and target as different objects. Printed p. 60 / PDF p. 87 shows a historical EUR/USD setup with the prior resistance, buffered entry, Kijun-based stop, separate alert and later “Preserve” stop explicitly labeled. That is the source's example, not a current market rule.

For the plugin, do not infer a precise price from the indicator name alone. On a live review, use actual completed candles and label each level with price zone, timeframe, timestamp/anchor and the evidence behind it. Describe an unbroken level as a candidate; test acceptance/rejection or a completed trigger before calling it support, resistance or a trade. If the chart feed lacks the plotted history or offset, mark the Chikou/cloud test unavailable instead of guessing.

## Strategies reviewed

The “ideal” foundation strategy (printed pp. 150–151 / PDF pp. 177–178) requires aligned cloud context, Tenkan/Kijun relationship, Chikou versus prior price, future cloud order, acceptable distance from the lines, and avoiding an obstructive thick cloud. Patel also describes four additional families: Tenkan/Kijun crossover, Kijun crossover, Kumo breakout and Senkou crossover. The book gives high-level directional conditions for these alternatives but explicitly does not provide complete entries, stops, exits or a fully tested trading plan for each.

Two useful process distinctions:

- **Alert vs setup vs entry:** in the historical plan, alerts are placed before a major support/resistance boundary so a subsequent breakout can be acted on; an alert by itself is not an entry. Confirm all conditions and the actual trigger on the decision bar.
- **Breakout failure:** Patel calls Kumo breakout his least favorite strategy and says cloud breaks can reverse on the next bar(s). Require the plan's close/confirmation and invalidate the setup when price re-enters or fails the defined level; do not mark every cloud cross as a trade.

The five strategies reuse the same underlying price-derived lines. Their agreement is correlated evidence, not five independent votes. Multi-timeframe confirmation must also use completed higher-timeframe bars and must not double-count the same move.

## Backtest and day-trading audit

The long worked example uses daily EUR/USD charts, a manually evaluated checklist and eight trades. It describes the test as Jan. 1, 2007–Nov. 9, 2009, while the results chapter labels the eight-trade table Jan. 1, 2007–Jan. 1, 2009 and the walkthrough ends in Oct./Dec. 2008. These dates do not reconcile. The chart-by-chart process also catches and rewinds an alert-placement mistake, which is a hindsight/look-ahead risk unless the correction is logged as a new test.

The post-analysis chapter changes rules after observing the same outcomes. It says the final 550-pip-exit table is an estimate rather than a complete rerun and tells readers to backtest it again. The sample is one historical FX pair and a small number of trades; the book supplies no independent replication, robust held-out period, modern BTC/Indian-market test or audited live execution. Treat all reported returns, “risk/reward” columns and “high probability” language as author-reported examples. Some tables have OCR/typographical ambiguities, and the columns use risk/reward inconsistently; recalculate from raw entry/exit/stop values before relying on a ratio.

Chapter 8's EUR/USD 5-minute test uses a manually illustrated Kijun cross → pullback → Tenkan entry sequence and rules such as two-loss/day and maximum-trades limits. Those are historical examples alongside a story about margin, no stop, a gap and account loss. Do not reuse its $250 capital, monthly income targets, pip buffers, forex spread, contract sizes, or stop/target numbers for BTC perpetuals, Indian cash/futures/options, or current venues. A stop can gap or slip; leveraged products can lose more than the planned stop estimate or be liquidated.

## Time elements, psychology and evidence boundaries

- The book lists time counts 9, 17, 26, 33, 42, 51, 65, 76, 83, 97, 101, 129, 172, 200 and 257; it derives many arithmetically from 9/26 and shows vertical lines from price-reversal anchors. Patel says he does **not** use Ichimoku time elements in his trading and prefers Gann. The listed ranges are broad/inconsistent; he argues against using the broad ranges and accepts at most ±1 in an example. Keep the entire time-count idea research-only, timestamp the swing anchors, and require independent out-of-sample evidence before any signal use.
- The psychology chapter argues for system fit, accepting loss streaks, avoiding increased bets after losses, testing a system on the intended instrument/conditions, and journaling the reason for entry and exit. Use these as process questions. The chapter's failure-rate and anecdotal claims are not independently verified. Its kinesiology/psychological interventions are not an evidence-backed plugin method and are not recommended here.
- Use price/market data from the connected provider, never from this 2010 book. The book's examples are historical U.S. stocks and FX, mostly 2007–2009; they establish neither current thresholds nor a BTC/India edge.
- For causal scans, calculate each indicator from data available at the signal timestamp. Never use the Chikou line as if its plotted historical point were known 26 bars earlier. Respect the 26-bar cloud offsets, completed-bar cutoff, exchange session, gaps, tick size, contract multiplier, fees, spread, slippage and funding. Do not test a strategy using visually shifted values that leak future data.
- No plugin detector, automatic scan, chart-editing action or profitability claim is added by this review. The note upgrades the book-grounded annotation and analysis workflow only.

## Reference policy

Use chapter, printed page and physical PDF page together when available. Key examples: formulae/levels, Ch. 1, printed pp. 4–40 (PDF pp. 31–67); Chikou-peak horizontal level, p. 25 (PDF p. 52); trading-plan table, pp. 43–44 (PDF pp. 70–71); entry/stop/alert chart, p. 60 (PDF p. 87); backtest critique/tables, Ch. 4, pp. 137–147 (PDF pp. 164–174); strategy caveats, Ch. 5, pp. 149–159 (PDF pp. 176–186); time methods, Ch. 6, pp. 161–169 (PDF pp. 188–196); day-trading risk/test, Ch. 8, pp. 181–192 (PDF pp. 208–219); worksheet, pp. 195–197 (PDF pp. 222–224). Cite only the source-specific concept that bears on the setup and state whether live evidence supports, contradicts or leaves it unresolved.
