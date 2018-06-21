import unittest

def swap(inputs, x, y):
    tmp = inputs[x]
    inputs[x] = inputs[y]
    inputs[y] = tmp

def mysolution(inputs):
    for x in range(inputs.count(0)):
        for i in range(len(inputs) - 1):
            if 0 == inputs[i]:
                swap(inputs, i, i+1)
    return inputs

def mysolution2(inputs):
    for i in range(len(inputs) - 1):
        if 0 == inputs[i]:
            swap(inputs, i, i+1)

solution = mysolution2

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([0, 17, 0, 3, 4]), [17, 3, 4, 0, 0])


if __name__ == '__main__':
    unittest.main()