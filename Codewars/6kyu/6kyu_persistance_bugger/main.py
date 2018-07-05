import unittest
import functools
import operator

def mysolution(n):
    cnt = 0
    while n and 1 < len(str(n)):
        n = functools.reduce(operator.mul, (int(i) for i in str(n)))
        cnt += 1
    return cnt

def othersolution(n):
    cnt = 0
    while n >= 10:
        n = functools.reduce(operator.mul, (int(i) for i in str(n)))
        cnt += 1
    return cnt

persistence = othersolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(persistence(39), 3)

    def test_2(self):
        self.assertEqual(persistence(4), 0)

    def test_3(self):
        self.assertEqual(persistence(25), 2)

    def test_4(self):
        self.assertEqual(persistence(999), 4)

if __name__ == '__main__':
    unittest.main()
