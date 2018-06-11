from math import floor
import unittest

def litres(time):
    # return floor(time * 0.5)
    return time // 2


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(litres(2), 1)

    def test_2(self):
        self.assertEqual(litres(1.4), 0)

    def test_3(self):
        self.assertEqual(litres(12.3), 6)

    def test_4(self):
        self.assertEqual(litres(0.82), 0)

    def test_5(self):
        self.assertEqual(litres(11.8), 5)

    def test_6(self):
        self.assertEqual(litres(1787), 893)

    def test_7(self):
        self.assertEqual(litres(0), 0)

if __name__ == '__main__':
    unittest.main()