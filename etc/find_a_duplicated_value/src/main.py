import unittest

def mysolution(inputs):
    dic = {}
    for value in inputs:
        if None == dic.get(value):
            dic[value] = value
        else:
            return value
    return -1

def mysolution2(inputs):
    for num in inputs:
        if num in set_:
            return num
        else:
            set_.add(num)
    return -1

solution = mysolution2

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1, 3, 2, 3, 4]), 3)

    def test_2(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), -1)


if __name__ == '__main__':
    unittest.main()