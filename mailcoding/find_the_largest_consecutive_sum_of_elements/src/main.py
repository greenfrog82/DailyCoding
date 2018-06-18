import unittest

def solution(inputs):
    from itertools import islice

    max_sum = current_sum = inputs[0]
    
    for value in islice(inputs, 1, None):
        current_sum = max(current_sum + value, value)
        max_sum = max(current_sum, max_sum)

    return max_sum
        
        
class Test(unittest.TestCase):
    def test_1(self):
        # 3 + (-1) + 5
        self.assertEqual(solution([-1, 3, -1, 5]), 7)

    def test_2(self):
    #     # -1
        self.assertEqual(solution([-5, -3, -1]), -1)

    def test_3(self):
    #     # 2 + 4 + (-2) + (-3) + 8
        self.assertEqual(solution([2, 4, -2, -3, 8]), 9)

    def test_4(self):
        self.assertEqual(solution([3, -1, -1, 2]), 3)
    
    def test_5(self):
        self.assertEqual(solution([3, -1, -1, 3]), 4)

    def test_6(self):
        self.assertEqual(solution([-1, -3, -5]), -1)

    def test_7(self):
        self.assertEqual(solution([2, 4, -2, 2, 8]), 14)

        
if __name__ == '__main__':
    unittest.main()        