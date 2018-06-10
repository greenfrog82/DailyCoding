import unittest

def get_sum(inputs):
    pass

class Test(unittest.TestCase):
    def test_1(self):
        # 3 + (-1) + 5
        self.assertEqual(get_sum([-1, 3, -1, 5]), 7)

    def test_2(self):
        # -1
        self.assertEqual(get_sum([-5, -3, -1]), -1)

    def test_3(self):
        # 2 + 4 + (-2) + (-3) + 8
        self.assertEqual(get_sum([2, 4, -2, -3, 8], 9))
        
        