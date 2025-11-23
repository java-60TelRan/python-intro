from unittest import TestCase
from ltr_evaluation import ltrEvaluation
class TestLtrEvaluation(TestCase):
    
    def test_ltr_eval(self):
        expr = "(3 + (2 * 10 / (40 - 20))+(3 * 4)) * 10"
        self.assertEqual(160, ltrEvaluation(expr))
        