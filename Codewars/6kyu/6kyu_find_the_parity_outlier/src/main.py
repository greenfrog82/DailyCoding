import unittest

def mysolution(integers):
    samples = [i%2 for i in integers]
    return integers[samples.index(1)] if len(integers)-1 == samples.count(0) else integers[samples.index(0)]

def othersolution(integers):
    samples = [i%2 for i in integers]
    return integers[samples.index(1)] if sum(samples) == 1 else integers[samples.index(0)]
    
def othersolution2(integers):
    odds = [num for num in integers if num%2]
    evens = [num for num in integers if not num%2]
    return odds[0] if len(odds) < len(evens) else evens[0]

find_outlier = othersolution

class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

unittest.main()