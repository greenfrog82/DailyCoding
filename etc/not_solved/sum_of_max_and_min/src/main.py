import unittest

def large_number(nums):
    pass

def small_number(nums):
    pass


def solution(nums):
    nums = sorted(nums)
    
        
class Test(unittest.TestCase):
    def test_large_number_1(self):
        self.assertEqual(large_number([2, 9, 10, 21, 24]), 92421210)

    def test_larget_number_2(self):
        self.assertEqual(large_number([1, 2, 3]), 321)

    def test_small_number_1(self):
        self.assertEqual(small_number([1,2,3]), 123)

    def test_small_number_2(self):
        self.assertEqual(small_number([2, 9, 10, 21, 24]), 10221249)

    def test_solution_1(self):
        self.assertEqual(solution([1,2,3]), 444)

    def test_solution_2(self):
        self.assertEqual(solution([2, 9, 10, 21, 24]), 102634359)
        

if __name__ == '__main__':
    unittest.main()
