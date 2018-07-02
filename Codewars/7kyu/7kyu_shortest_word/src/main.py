import unittest
from functools import reduce

def mysolution(str):
    return min(len(i) for i in str.split())

def othersolution(str):
    return len(min(str.split(), key=len))

find_short = othersolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)

    def test_2(self):
        self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)

    def test_3(self):
        self.assertEqual(find_short("lets talk about javascript the best language"), 3)

    def test_4(self):
        self.assertEqual(find_short("i want to travel the world writing code one day"), 1)

    def test_5(self):
        self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)

if __name__ == '__main__':
    unittest.main()