import unittest
import math

def mysolution(n):
    return False if 0 > n else 0 == int(str(math.sqrt(n)).split('.')[1])

def othersolution(n):
    return n > -1 and math.sqrt(n) % 1 == 0

def othersolution2(n):
    return n == int(n**.5)**2 if n >= 0 else False

def othersolution3(n):
    return math.sqrt(n).is_integer() if 0 <= n else False

def othersolution4(n):
    return n == (n//2)**2 if n >= 0 else False

is_square = othersolution4

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
        self.assertEqual(is_square(0), True, "0 is a square number")
        self.assertEqual(is_square(3), False, "3 is not a square number")
        self.assertEqual(is_square(4), True, "4 is a square number")
        self.assertEqual(is_square(25), True, "25 is a square number")
        self.assertEqual(is_square(26), False, "26 is not a square number")

if __name__ == '__main__':
    unittest.main()