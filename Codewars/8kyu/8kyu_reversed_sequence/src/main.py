import unittest

def reverse_seq(n):
    return list(range(n, 0, -1))


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_seq(5), [5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()
