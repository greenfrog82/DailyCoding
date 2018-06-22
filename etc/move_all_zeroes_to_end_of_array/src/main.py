import unittest

def swap(inputs, x, y):
    inputs[x], inputs[y] = inputs[y], inputs[x]

# Time : O(n) 
# Space : O(n)
def mysolution(inputs):
    arr_with_zero = [i for i in inputs if 0 == i]
    arr_with_out_zero = [i for i in inputs if 0 != i]

    return arr_with_out_zero + arr_with_zero

# Time : O(n^2)
# Space : O(1)
def mysolution2(inputs):
    for x in range(inputs.count(0)):
        for i in range(len(inputs) - 1):
            if 0 == inputs[i]:
                inputs[i], inputs[i+1] = inputs[i+1], inputs[i]
    return inputs

# Time : O(nlogn)
# Space : ?
def mysolution3(inputs):
    return sorted(inputs, key=lambda k:0==k)

# Time : O(n)
# Space : O(1)
def mysolution4(inputs):
    count = 0
    
    for idx, value in enumerate(inputs):
        if 0 != value:
            inputs[count] = value
            count += 1

    for i in range(len(inputs) - count):
        inputs[count+i] = 0
    
    return inputs
    

solution = mysolution4

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([0, 17, 0, 3, 4]), [17, 3, 4, 0, 0])

    def test_2(self):
        self.assertEqual(solution([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_3(self):
        self.assertEqual(solution([1,2,3,4,5]), [1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()