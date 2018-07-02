import unittest

def mysolution(numbers):
    ret = sorted(map(int, numbers.split(' ')))
    return '%d %d' % (ret[-1], ret[0])

def othersolution(numbers):
    numbers = [int(i) for i in numbers.split(' ')]
    return '%i %i' % (max(numbers), min(numbers))

def othersolution2(numbers):
    numbers = list(map(int, numbers.split(' ')))
    return '{} {}'.format(max(numbers), min(numbers))

def othersolution3(numbers):
    numbers = sorted(numbers.split(' '), key=int)
    return '{} {}'.format(numbers[-1], numbers[0])

high_and_low = othersolution3

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")

if __name__ == '__main__':
    unittest.main()