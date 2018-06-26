import unittest

def mysolution(arr):
    if not arr:
        return arr
        
    stack = [arr[0]]
    
    for i in range(1, len(arr)):
        if stack:
            if 'NORTH' == stack[-1] and 'SOUTH' == arr[i] or 'SOUTH' == stack[-1] and 'NORTH' == arr[i]:
                stack.pop()
            elif 'WEST' == stack[-1] and 'EAST' == arr[i] or 'EAST' == stack[-1] and 'WEST' == arr[i]:
                stack.pop()
            else:
                stack.append(arr[i])
        else:
            stack.append(arr[i])

    return stack

dirReduc = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
    
    def test_2(self):
        self.assertEqual(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])

    def test_3(self):
        self.assertEqual(dirReduc([]), [])
    

if __name__ == '__main__':
    unittest.main()