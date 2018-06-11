import unittest

def count_by(x, n):
    return range(x, x * n + 1, x)
    # return [i * x for i in range(1, n+1)]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(list(count_by(1, 5)), [1, 2, 3, 4, 5])

    def test_2(self):
        self.assertEqual(list(count_by(2, 5)), [2, 4, 6, 8, 10])
    
    def test_3(self):
        self.assertEqual(list(count_by(3, 5)), [3, 6, 9, 12, 15])

    def test_4(self):
        self.assertEqual(list(count_by(50, 5)), [50, 100, 150, 200, 250])

    def test_5(self):
        self.assertEqual(list(count_by(100, 5)), [100, 200, 300, 400, 500])


if __name__ == '__main__':
    unittest.main()
