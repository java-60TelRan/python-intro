from unittest import TestCase
from ltr_evaluation import ltrEvaluation
class TestLtrEvaluation(TestCase):
    
    def test_ltr_eval(self):
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertAlmostEqual(160.0, ltrEvaluation(expr),places=1)
        expr = "((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55"
        self.assertAlmostEqual(((3.5 + (2 * 10.45 / (40.5 - 40))+(3 * 4)) * (10.2 ** 2)) / 2.55, ltrEvaluation(expr),places=1)
        with self.assertRaises(ValueError):
            ltrEvaluation("4 + 2   5")
        with self.assertRaises(ZeroDivisionError):
            ltrEvaluation("4 + 2  / (20 / 20 - 1)")
        