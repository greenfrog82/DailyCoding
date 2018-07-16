import unittest

def mysolution(arr):
    for i in xrange(len(arr) - 1):
        if 0 == i == sum(arr[i+1:]):
            return 0
        else:
            left_sum = sum(arr[:1+i])
            right_sum = sum(arr[i+2:])

            if left_sum == right_sum:
                return i+1
    return -1

def othersolution(arr):
    for i in xrange(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

find_even_index = othersolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        self.assertEqual(find_even_index([1, 100, 50, -51, 1, 1]), 1)
        self.assertEqual(find_even_index([1, 2, 3, 4, 5, 6]), -1)
        self.assertEqual(find_even_index([20, 10, 30, 10, 10, 15, 35]), 3)
        self.assertEqual(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
        self.assertEqual(find_even_index([10, -80, 10, 10, 15, 35, 20]), 6)
        self.assertEqual(find_even_index(range(1, 100)), -1)
        self.assertEqual(find_even_index([0, 0, 0, 0, 0]), 0, "Should pick the first index if more cases are valid")
        self.assertEqual(find_even_index([-1, -2, -3, -4, -3, -2, -1]), 3)
        self.assertEqual(find_even_index(range(-100, -1)), -1)

if __name__ == '__main__':
    unittest.main()