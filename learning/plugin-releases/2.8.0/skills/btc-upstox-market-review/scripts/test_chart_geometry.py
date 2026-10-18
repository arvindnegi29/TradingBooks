import unittest
from chart_geometry import line_value, projection


class GeometryTests(unittest.TestCase):
    def test_scale_changes_line_not_prices(self):
        a=[{'bar':0,'price':100,'known_at_bar':2},{'bar':2,'price':121,'known_at_bar':4}]
        self.assertAlmostEqual(line_value(a,1,4,'log')['price'],110)
        self.assertEqual(line_value(a,1,4,'linear')['price'],110.5)
        self.assertEqual(line_value(a,1,4,'linear')['status'],'retrospective_line_value')
        self.assertFalse(line_value(a,1,4,'linear')['causal_at_evaluation_bar'])

    def test_future_confirmation_unavailable(self):
        a=[{'bar':0,'price':100,'known_at_bar':2},{'bar':2,'price':121,'known_at_bar':4}]
        with self.assertRaises(ValueError): line_value(a,3,3,'linear')
        self.assertEqual(line_value(a,6,4,'linear')['status'],'future_projection')

    def test_head_neckline_measurement_not_box_height(self):
        p=projection('head_shoulders','down',head=17,neckline_at_head=14.47,breakout=15.05)
        self.assertAlmostEqual(p['target'],12.52)
        self.assertEqual(projection('head_shoulders','up',head=80,neckline_at_head=90,breakout=92)['target'],102)

    def test_swing_projects_from_old_extreme(self):
        self.assertAlmostEqual(projection('swing','up',old_extreme=29.17,retracement_extreme=25.02)['target'],33.32)
        self.assertAlmostEqual(projection('swing','down',old_extreme=45.26,retracement_extreme=60.44)['target'],30.08)

    def test_flag_and_gap_have_different_bases(self):
        self.assertEqual(projection('flag','up',pole_start=80,pole_end=100,prebreak_extreme=94)['target'],114)
        self.assertAlmostEqual(projection('continuation_gap','up',trend_start=18.95,gap_midpoint=21.57)['target'],24.19)
        self.assertEqual(projection('height','down',high=110,low=100,breakout=102)['target'],92)

    def test_bad_inputs_rejected(self):
        for value in [float('nan'),float('inf'),True]:
            with self.assertRaises(ValueError):projection('height','up',high=value,low=1,breakout=2)
        with self.assertRaises(ValueError):projection('swing','up',old_extreme=80,retracement_extreme=90)
        with self.assertRaises(ValueError):projection('head_shoulders','down',head=80,neckline_at_head=90,breakout=85)


if __name__=='__main__':unittest.main()
