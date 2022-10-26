import unittest

from src.utility.utility import Utility


class TestUtilityUtility(unittest.TestCase):
    def test_order_max_min(self):
        util = Utility()
        min, max = util.order_min_max(5,2)
        self.assertEqual(min,2)
        self.assertEqual(max,5)


if __name__ == '__main__':
    unittest.main()
