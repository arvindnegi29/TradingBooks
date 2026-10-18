# *Timing Solutions for Swing Traders* — complete review

**Authors:** Robert T. H. Lee (Chapters 1–8); Peter A. Tryde (Chapter 9)  
**Edition/year:** Wiley, 2012  
**Source:** user-uploaded PDF, 242 physical pages; SHA-256 `3af3fade2ba221d6fb145a4517ddfc9fb7210715be873bb4a2d36f11142179a`  
**Coverage:** extracted text reviewed in page order across all 242 PDF pages, including the 11 blank pages, all chapters, appendices, formulas, glossary, bibliography, author notes and index. Selected figures and chart pages were visually inspected (PDF pp. 172–173, 179 and 201); this is not an exhaustive image-by-image visual audit. No strategy was independently replicated or validated.

## Chapter map and transferable ideas

| Source pages | Material and usable lesson | Transfer boundary |
|---|---|---|
| 1–11 | Title, contents, foreword, preface, disclaimer. The authors describe discretionary end-of-day swing trading and say their sample system was not automated or optimized. | The book itself warns that methods may not be profitable. |
| 12–20, Ch. 1 | Trading psychology, technical/fundamental analysis, avoiding overanalysis and redundant indicators. Treat price pattern, volume, momentum and moving-average evidence as different dimensions; repeated transforms of the same prices are not independent confirmation. | A checklist organizes evidence; it does not prove predictive power. |
| 21–42, Ch. 2 | Four-dimension technical scorecard, multi-timeframe reading and a separate financial-astrology overview. Context should precede individual triggers. | Astrology assertions are hypotheses/examples, not established signal evidence. |
| 43–74, Ch. 3 | Candlestick context; double tops/bottoms, head-and-shoulders, rectangles, saucers/cup-and-handle, AB=CD, gaps, divergence and diagonal/Wolfe patterns. Wait for activation/price confirmation; treat measured moves as estimates. | Historical stock examples are not a quantified BTC or options edge. Pattern rules vary by instrument and timeframe. |
| 75–108, Ch. 4 | Elliott impulse/corrective structures, alternation and Fibonacci proportions. The book states the count is subjective and advises higher-timeframe focus rather than counting every fluctuation. | Alternative counts are unavoidable; ratios are guides, not calibrated targets. Use as a descriptive scenario only. |
| 109–118, Ch. 5 | Volume-at-price context, relative volume, and Volume Zone Oscillator (VZO). Read activity against the instrument’s own baseline and price progress; one bar alone is weak evidence. | VZO settings are author choices. Match data to venue/contract; do not infer buyer identity, institutional intent or open/close activity from OHLCV alone. |
| 119–141, Ch. 6 | Data adjustment, uncluttered chart layout, momentum, trend/moving averages, MACD, ADX and ATR. Moving averages lag and whipsaw; ADX measures strength, not direction. | Do not copy formulas without implementation tests. The author says the ATR stop formula is not recommended for trading (p. 139). |
| 142–160, Ch. 7 | A discretionary trend workflow: weekly context with daily execution, short/mid/long averages, momentum and volume; plus Ichimoku cloud/lines as dynamic context. | It is an example workflow, not a frozen or optimized system. Its stock-market session assumptions do not transfer directly to 24/7 BTC or Indian options. |
| 161–168, Ch. 8 | Trading plan, instrument/timeframe selection, liquidity, entries/exits, risk planning, journal and checklists. | The book’s suggested risk percentages and reward ratios are personal/historical guidance, not plugin defaults or universal recommendations. Use the user’s risk budget and current contract/liquidity data. |
| 169–205, Ch. 9 | Financial astrology: new/full moon rules, eclipse and planetary-cycle claims, astro-screening after technical scans, personal natal-chart timing, Part of Fortune, and software-generated market projections. | Keep all astro claims out of live signal confirmation. The chapter uses selected historical examples, some hand-waved causal stories and optimized projections; its own charts show forecast timing/scale misses. No BTC or Indian options validation. |
| 206–210, Apps. 1–3 | Traditional astrology house rulerships, aspects and zodiac/industry mappings. | Descriptive record of the authors’ astrological framework, not empirical market evidence. |
| 211–217, App. 4 | MetaStock formula listings for oscillators, VZO, moving-average mirror lines and midterm averages. | Educational source code only; several expressions need parser and data checks before any reproduction. Page 217 itself ends with an educational-only disclaimer. |
| 218–222 | Technical and astrological glossary. | The astrology vocabulary documents the method, not its validity. |
| 223–242 | Bibliography, software/resources, author biographies and index. | Vendor references, URLs and software are historical (2012). |

## Use in a BTC/India review

Borrow the **process**, not the book’s untested settings: establish the requested horizon and venue; describe higher-timeframe trend/levels; identify the actual price-pattern trigger and invalidation; compare relative volume with a relevant baseline; use momentum/MA information as context; name when evidence is redundant; and show a contrary case. A chart annotation should label observed swing highs/lows, range boundaries, breakout/retest status, timeframe and invalidation. Mark zones as zones when price interaction is broad; do not imply false precision. Cite this book only for its own concepts and page numbers, and separately identify the live observation/calculation.

For BTC, use the requested exchange’s own 24/7 candles and venue-specific derivatives data. For Indian instruments, respect market hours, underlying/contract identity, expiry, corporate-action adjustments and actual options liquidity. The book studies mainly Hong Kong equities with end-of-day bars; its examples cannot establish thresholds, expectancy, entry rules or risk sizing for these markets. Its discretionary trend method should not be silently converted into a mechanical screen.

### Source inconsistencies and implementation cautions

- PDF p. 122 reverses the classic divergence descriptions: its bearish example says oscillator lower lows while price makes higher highs, and its bullish example says oscillator higher highs while price makes lower lows. This conflicts with the standard descriptions in the same book (including p. 52). Follow the actual price/oscillator relationship, not the mislabeled text.
- PDF p. 130 describes a bearish moving-average order inconsistently: it says 50-day below 90-day and 90-day above 200-day. Verify ordering against the intended rule before coding.
- Formula examples contain apparent naming/variable inconsistencies (including p. 153 and Appendix 4). Do not copy into a scan/backtest without compiling, unit-checking inputs, and comparing outputs with hand calculations.
- Elliott counts, pattern measurements, Ichimoku interpretations and the “four dimensions” remain judgment aids. Scorecard agreement is not independent if several signals reuse the same price series.

## Financial astrology: source claims versus research evidence

Tryde describes buying at a new moon and selling at a full moon, planetary aspects, first-trade stock charts and personal natal timing (PDF pp. 170–205). The chapter says technical analysis should filter lunar timing (pp. 172–173), but also makes strong claims that astro-scans improve selection (pp. 178–185) without a prospective, blinded or cost-adjusted comparison. The examples are selected after events and the projection software optimizes historical correlations. The authors concede the projection is not an entry/exit signal, its scaling is rarely fully accurate, and cycle changes constrain the sample (pp. 200–204). The chapter’s proposed “harmonic resonance” mechanism (p. 205) is not an empirical demonstration.

Published research is mixed and remains specific to its samples and methods: Yuan, Zheng and Zhu (2006) report lower returns around full than new moons in 48 country indices; Keef and Khaled (2011), using a different specification and 62 indices, find an enhanced new-moon effect but no overall full-moon effect; Reschenhofer and Lingler (2013) find no significant lunar relationship and attribute earlier contradictory results to methods/data snooping. A 2021 India study reports an association for Mercury retrograde in NIFTY 50 and Sensex, but it examines only two daily index series and does not validate an actionable rule for BTC, intraday trading or options. These findings do not justify a trading signal or imply causation.

If a user explicitly asks to research astrology, isolate it as a **non-actionable research hypothesis**: pre-register the market, dates/aspects, signal, horizon, benchmark, costs and test; use point-in-time data and no look-ahead; compare against seasonal/random controls; correct for multiple testing; freeze the rule before a truly untouched out-of-sample period; report uncertainty and adverse regimes. Keep results separate from the live trade verdict until independently validated. Do not let it increase confidence, size, or override a price invalidation.

## External research references

- Yuan, Kathy, Lu Zheng, and Qiaoqiao Zhu. “Are Investors Moonstruck? Lunar Phases and Stock Returns.” *Journal of Empirical Finance* 13(1), 2006, pp. 1–23. DOI: [10.1016/j.jempfin.2005.06.001](https://doi.org/10.1016/j.jempfin.2005.06.001).
- Keef, Stephen P., and Mohammed S. Khaled. “Are Investors Moonstruck? Further International Evidence on Lunar Phases and Stock Returns.” *Journal of Empirical Finance* 18(1), 2011, pp. 56–63. DOI: [10.1016/j.jempfin.2010.11.002](https://doi.org/10.1016/j.jempfin.2010.11.002).
- Reschenhofer, Erhard, and Michaela Lingler. “Detecting Synchronous Cycles in Financial Time Series of Unequal Length.” *Journal of Empirical Finance* 24, 2013, pp. 1–9. DOI: [10.1016/j.jempfin.2013.07.003](https://doi.org/10.1016/j.jempfin.2013.07.003).
- Mahendra, Ashish, Shiba Prasad Mohanty, and S. Sudalaimuthu. “Financial Astrology and Behavioral Bias: Evidence from India.” *Asia-Pacific Financial Markets* 28(1), 2021, pp. 3–17. DOI: [10.1007/s10690-020-09310-8](https://doi.org/10.1007/s10690-020-09310-8).

For plugin use, cite Lee/Tryde for the book’s stated technical workflow and historical astrology claims, but never present astrology as confirmation or as a validated live BTC/Indian-market signal. The transferable additions are multi-timeframe context, nonredundant evidence, observed-level annotation, confirmation/invalidation, risk planning and a written review trail.
