from unittest import TestCase


class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(6, sum([0, 2, 3]), "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(6, sum((1, 2, 3)), "Should be 6")