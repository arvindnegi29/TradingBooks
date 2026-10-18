"""Independent arithmetic checks of selected source-review findings.
These are not strategy backtests and do not validate any market edge.
Run: python test_chan_review.py
"""
import unittest

class SourceReviewChecks(unittest.TestCase):
    def test_long_return_sign(self):
        entry, exit_price, side = 100.0, 110.0, 1
        self.assertAlmostEqual(side * (exit_price-entry)/entry, 0.10)
        self.assertAlmostEqual(side * (entry-exit_price)/entry, -0.10)

    def test_short_return_sign(self):
        entry, exit_price, side = 100.0, 90.0, -1
        self.assertAlmostEqual(side * (exit_price-entry)/entry, 0.10)
        self.assertAlmostEqual(side * (entry-exit_price)/entry, -0.10)

    def test_displayed_johansen_eigen_first_rank(self):
        statistic, critical_95 = 16.897, 21.131
        self.assertFalse(statistic > critical_95)

    def test_gap_loss_can_exceed_stop_budget(self):
        entry, stop, next_executable = 100.0, 95.0, 80.0
        self.assertGreater(entry-next_executable, entry-stop)

    def test_growth_curvature_uses_variance(self):
        mean, variance, leverage = 0.30, 0.26**2, 2.0
        usual_second_order_growth = leverage*mean - leverage**2*variance/2
        suspect_mean_squared_growth = leverage*mean - leverage**2*mean**2/2
        self.assertNotAlmostEqual(usual_second_order_growth, suspect_mean_squared_growth)

if __name__ == "__main__":
    unittest.main()
