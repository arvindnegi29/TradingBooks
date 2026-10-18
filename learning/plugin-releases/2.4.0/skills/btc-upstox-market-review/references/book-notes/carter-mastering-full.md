# John F. Carter - Mastering the Trade, second edition (2012)
## Source and review limits
Complete extracted-text review of all 525 physical PDF pages, including front matter, all 26 chapters, conclusion, index, biography and final linked contents fragment. Root reader reviewed 1-77; six chapter readers reviewed 78-179,180-270,271-344,345-432,433-494,495-525 respectively. All reported full sequential coverage; initially truncated outputs were reread in smaller complete batches before counting coverage. This is a coordinated full-text review, with selected chart/table inspection, not every chart pixel, equation proof, strategy replication or empirical validation. Never claim the model was trained or that any strategy became profitable through reading.
Source title page: John F. Carter, McGraw-Hill 2012; electronic ISBN 978-0-07-178826-7.
Uploaded file: Mastering the Trade - Proven Techniques for Profiting from Intraday and Swing Trading Setups 2nd edition 2012 (1) - annotated(1).pdf.
SHA256: 324e5091c2e5bf138f749deb1447e26aaf97efa403b321b139dfd9ad55930aff.
Git blob computed from uploaded bytes: d5b11415b61bbfb6934879af581d65935d8ff0c0; matches exact New Folder catalog entry. Do not transfer coverage to a different edition merely by title.
Source: https://github.com/arvindnegi29/TradingBooks/blob/284a6c51261a6d7fb7499f4eb00ca20c60d554fa/New%20Folder/Mastering%20the%20Trade%20-%20Proven%20Techniques%20for%20Profiting%20from%20Intraday%20and%20Swing%20Trading%20Setups%202nd%20edition%202012%20(1)%20-%20annotated.pdf
Cite 1-based physical PDF pages, never a guessed constant print offset. PDF bookmarks erroneously send many chapters to page2; chapter starts below were checked against actual content. Final525 is a real linked contents fragment, not another chapter. Conclusion ends508; index509-523; bio524.
The PDF contains233 embedded annotations. Inspected early annotations are highlights with empty comment strings. Highlights are reader markup, not author endorsement or independent evidence. No exhaustive annotation audit claimed.
Detailed reading notes are paraphrases of the uploaded source; they are not implementations, new market observations or independently verified current law/specifications.

## Retrieval map
Read only applicable notes for a signal, rather than treating every chapter as a separate vote.
| Chapters | PDF pages | Detailed note |
|---|---|---|
| Front matter;1 psychology/failed high;2 discipline;3 technology;4 futures mechanics |1-77|[Review1-77](carter-pdf001-077.md)|
|5 options;6 internals;7 opening gap;8 pivots |78-179|[Review78-179](carter-pdf078-179.md)|
|9 tick fades;10 mean reversion;11 squeeze |180-270|[Review180-270](carter-pdf180-270.md)|
|12 waves;13 trend bars;14 scalper;15 bricks;16 ping-pong;17 end-of-day |271-344|[Review271-344](carter-pdf271-344.md)|
|18 boxes;19 HOLP/LOHP;20 gold/Darvas;21 TTM multi-timeframe |345-432|[Review345-432](carter-pdf345-432.md)|
|22 propulsion;23 premarket;24 business plan |433-494|[Review433-494](carter-pdf433-494.md)|
|25 troubleshooting;26 professional process; back matter |495-525|[Review495-525](carter-pdf495-525.md)|

Exact chapters:
1 15-27;2 28-41;3 42-55;4 56-77;5 78-86;6 87-125;7 127-144;8 145-179;9 180-206;10 207-215;11 216-270;12 271-277;13 278-281;14 282-304;15 305-319;16 320-331;17 332-344;18 345-365;19 366-381;20 382-401;21 402-432;22 433-453;23 455-476;24 477-494;25 495-500;26 501-508. Part dividers14,126,454.

## Mandatory application: source concept, implementation, evidence
For each applicable concept state (a) author's historical source rule, (b) local implementation/assumptions or unavailable status, (c) current observations, (d) validation status and contrary evidence. Never turn a source-reviewed narrative into a detector that has not actually been calculated.

### Regime before setup (Ch6,9-12)
Separate range/fade, directional continuation, volatility compression/release and reversal. A persistent one-sided trend invalidates simplistic fade-every-extreme logic; a squeeze can conflict with RTM band containment. Identify the mechanism/horizon first, and do not retrospectively switch variants to justify a position.
NYSE $TICK means net upticking versus downticking stocks. It is not BTC trade-count ticks, minimum price increment, CVD or order-book imbalance. TRIN is breadth/volume context; PCR population can be US option volume rather than NSE OI. Missing inputs remain unavailable, not replaced by a similarly named metric. Historical US thresholds and clock times are not BTC/Indian rules.
Compression is a developing condition, not an entry. BB20/2 and KC20/1.5 with momentum12 are disclosed source ingredients, but proprietary TTM histogram/Waves/Trigger/Trend exact algorithms are not fully specified. State formula, smoothing, source, bar inclusion and differences before using a public proxy; label the proxy separately. Do not fabricate WaveC from EMA or infer TTM output from a chart's color.

### Causality before visual pattern (Ch1,8,14,18-19,21-23)
Use completed trigger bars and higher-timeframe bars available at that instant. A higher-timeframe final close cannot be filled backwards over its component bars. Confirmed pivots become known only after their right-hand confirmation bars.
Scalper markers can be painted on an earlier bar only after a third bar closes (PDF282-284). Never backtest an entry at the retroactively marked first bar. Exact proprietary/filter ambiguity remains unimplemented.
Define box tests, boundaries, tolerance, expiry, failed-breakout anchors, HOLP/LOHP extreme-bar update and exits prospectively. Do not pick the eventual lowest/highest bar with future knowledge. Discretionary examples require operational definitions before testing.
Trade-count bars (e.g.233/377/987 trades) are not minute bars or volume bars. No exact tick-bar study from OHLCV minute data.
Period scaling across timeframes is not equality: two-minute SMA500 is not mathematically the same as five-minute SMA200; 15-minute EMA208/546 does not exactly reproduce daily EMA8/21. Use true aligned series.

### Risk and execution before direction (Ch1-5,10,18,22,24-26)
Planned stop loss is not a guaranteed maximum loss. Stop-market can slip, stop-limit can remain unfilled, gaps/outages/thin depth can invalidate the assumed fill. A stop moved to entry is not net breakeven after costs. Margin/collateral is not a separate insured balance and does not measure economic risk.
Size from the user's applicable cash budget, exact multiplier/currency/lot, structural distance and realistic costs; round down. If minimum lot exceeds budget, NO TRADE. Do not import book percentages, fixed US stop points, contract counts, profit quotas, 2.5x plateau targets or automatic replenishment of a wiped-out stake.
Scaling must have a precommitted total risk cap and feasible lots. Separate alternative exit rules rather than mixing signal-only, ATR, pivot and trend-bar exits after seeing outcome. Never remove protective risk controls or double/reverse a position under the guise of closing it. No automatic orders/hedges, leverage change, account queries or transfers.
BTC requires actual venue volume/units, 24/7 session definition and funding. NSE requires actual session, contract/expiry/lot/tick. Roll-created chart gaps are not BTC perpetual funding or FVG; cash-open stock gaps are not arbitrary UTC gaps. Official settlement and last close are different; disclose any proxy used for pivots.

### Options (Ch5,10,22,26)
Use intrinsic/extrinsic value correctly: option premium is total quoted price; the author sometimes calls only extrinsic value premium. ITM/abs(delta) around0.70 is an author's preference, not a guaranteed optimal strike, fill, return or safety threshold.
Delta times underlying move is only a local approximation; actual premium scenario needs elapsed time, gamma, IV/vega/theta, bid/ask and contract units. IV crush can overcome correct direction; premium is not generally linear in IV.
Long monthly/short weekly is a different-expiry diagonal/calendar structure, not an ordinary same-expiry vertical. Do not import American assignment/delivery assumptions into Indian/BTC contracts. High IV alone does not validate naked selling.
Book examples and underlying target levels never substitute for fresh executable option quotes or a supported pricing method.

### Process and review (Ch2,23-26)
Use top-down context and a compact state table: context, developing trigger, confirmed trigger, invalidation, unavailable inputs. Related timeframes, indicators and price structures are correlated evidence, not independent probability multipliers.
Keep consecutive trade ledgers, setup version, confirmation/fill timestamps, costs, exit reason and compliance. Separate a valid losing trade from a rule violation; a winning impulse trade does not validate the process. A25-trade block is an educational review unit, not proof of edge. No parameter tweaking after one or two losses or repeated selection on the same holdout.
Paper trading remains useful for learning/replay/forward testing; do not require real-money losses to demonstrate discipline. Treat psychological typologies, success percentages, health regimens and medical claims as unsupported by this source review, not plugin advice. Optional rest/journal preferences do not diagnose the user.
Historical author/student drawdown pauses and two-stopout rules are distinct examples, not universal/current risk defaults. Verify material event schedules; the author's news-dismissal opinions do not remove event risk checks.

## Source audit and limits
Selected printed errors/ambiguities require caution. They are not a corrected historical P&L series:
- PDF65:23 advancing stocks later11, yet prose calls it stronger; the counts weaken.
- PDF71-72: purported240USD equivalent stops include237.50 and250 using printed multipliers. Enforce tick/size rounding.
- PDF74: inconsistent EUR/USD caption and exchange-rate numbers; pip values require actual base units.
- PDF81/85: negative put-delta wording and different-expiry spread classification need careful interpretation.
- PDF161: Russell stops don't match the stated1.50point rule. PDF187/189/193 have direction/target/P&L arithmetic inconsistencies.
- PDF298:111.12 to112.10 is98pips, not95. PDF336:1099 to1100.50 is1.50points, not2.50. PDF337:10311 to10322 is11, not21.
- PDF344: author states original3:52 edge degraded/crowded; replacement internals adjustments are not fully specified. Mark historical/degraded, not a current ready signal.
- PDF384 simplifies ATR to high-low; use true range including previous-close gaps. PDF396 says ATR above20 where chart/prior rule indicates ADX.
- PDF441:87.95 times1.08 is94.986, not95.78. PDF470: given H1158.75/L1122/C1144.50 imply pivot1141.75, not displayed1144.75.
- PDF506-507 Fibonacci1.272/1.618 are multipliers (127.2%/161.8%), not1.272%/1.618%. Claimed85%/65% target probabilities lack supporting sample methodology here.
Do not advertise any source win-rate, crash-prediction claim, certainty of institutional intent, money-supply story or guaranteed hedge as verified evidence. Selected historical charts do not establish current BTC/Indian expectancy.

Independent arithmetic audit checked the TASR planned/gap/actual losses, recovery math and selected futures/pivot/example calculations. These are arithmetic checks, not strategy tests.
No new executable Carter detectors were added, no live signal behavior tested, and no Carter strategy was empirically backtested by this review. Preserve Chan's out-of-sample safeguards and the existing six BTC model failures. Consult new-folder-progress.json for subsequent book coverage; Coulling remains Chapter1 partial.

## Visual coverage ledger
Selected visuals, not an exhaustive full-resolution audit:
- Reader1:1,2,18,19,20,21,22,25,26,27,47,48,50,51,52,53,54,57,59,60,61,64,66,67,69,71,72,73,74,75 (full size25,26,69,74).
- Reader2:79,81,84,89,91,93,95,97,99,101,103,105,107,109,111,113,116,118,129,130,143,145,149,151,153,160,161,173,175,177.
- Reader3:182,200,202,203,208,209,215,219,220,225,226,240,242,254,270.
- Reader4:275,279,282,284,305,306,320,332,336,337,344.
- Reader5:346,348,354,362,364,380,389,393,396,398,399,401,403,411,423,429.
- Reader6:434,437,439,440,441,442,451,456,458,461,464,465,466,468,469,470,471,480,489.
- Reader7:499,500,505,507,525.
