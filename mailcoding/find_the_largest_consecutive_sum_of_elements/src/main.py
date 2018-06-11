from collections import OrderedDict
import functools
import unittest

def find_the_largest_consecutive_sum_of_elements(inputs):


class Test(unittest.TestCase):
    def test_1(self):
        # 3 + (-1) + 5
        self.assertEqual(find_the_largest_consecutive_sum_of_elements([-1, 3, -1, 5]), 7)

    # def test_2(self):
    #     # -1
    #     self.assertEqual(find_the_largest_consecutive_sum_of_elements([-5, -3, -1]), -1)

    # def test_3(self):
    #     # 2 + 4 + (-2) + (-3) + 8
    #     self.assertEqual(find_the_largest_consecutive_sum_of_elements([2, 4, -2, -3, 8]), 9)
        
if __name__ == '__main__':
    unittest.main()        