import unittest

def two_sum(numbers, target):
    return next((i, numbers.index(target-v, i+1)) for i,v in enumerate(numbers) if target-v in numbers)    
    

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sorted(two_sum([1, 2, 3], 4)), [0, 2])

    def test_2(self):
        self.assertEqual(sorted(two_sum([1234, 5678, 9012], 14690)), [1, 2])

    def test_3(self):
        self.assertEqual(sorted(two_sum([2, 2, 3], 4)), [0, 1])


if __name__ == '__main__':
    unittest.main()