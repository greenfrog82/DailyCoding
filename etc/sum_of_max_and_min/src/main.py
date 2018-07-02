import unittest
from functools import cmp_to_key

def get_sorted_nums(nums):
    return sorted(map(str, nums), key=cmp_to_key(lambda x, y: int(x+y)-int(y+x)))

def large_number(nums):
    return int(''.join(reversed(get_sorted_nums(nums))))

def small_number(nums):
    return int(''.join(get_sorted_nums(nums)))

def solution(nums):
    return large_number(nums) + small_number(nums)
    
    
class Test(unittest.TestCase):
    def test_large_number_1(self):
        self.assertEqual(large_number([2, 9, 10, 21, 24]), 92422110)

    def test_larget_number_2(self):
        self.assertEqual(large_number([1, 2, 3]), 321)

    def test_larget_number_3(self):
        self.assertEqual(large_number([3, 30, 34, 5, 9]), 9534330)

    def test_small_number_1(self):
        self.assertEqual(small_number([1,2,3]), 123)

    def test_small_number_2(self):
        self.assertEqual(small_number([2, 9, 10, 21, 24]), 10212249)

    def test_solution_1(self):
        self.assertEqual(solution([1,2,3]), 444)

        self.assertEqual(solution([2, 9, 10, 21, 24]), 102634359)
        

if __name__ == '__main__':
    unittest.main()