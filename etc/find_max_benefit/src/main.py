import unittest
import itertools

def solution(inputs):
    min_value = min(inputs)
    min_value_idx = inputs.index(min_value)
    
    if len(inputs)-1 == min_value_idx:
        return 0

    max_value = max(itertools.islice(inputs, inputs.index(min_value)+1, None))
    return max_value - min_value


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([7, 1, 5, 3, 6, 4]), 5)

    def test_2(self):
        self.assertEqual(solution([7, 6, 4, 3, 1]), 0)


if __name__ == '__main__':
    unittest.main()
