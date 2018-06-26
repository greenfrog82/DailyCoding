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

def othersolution(arr):
    opposite = {'NORTH':'SOUTH', 'EAST':'WEST', 'SOUTH':'NORTH', 'WEST':'EAST'}
    new_plan = []

    for d in arr:
        if new_plan and opposite[d] == new_plan[-1]:
            new_plan.pop()
        else:
            new_plan.append(d)

    return new_plan

def othersolution2(arr):
    str = ' '.join(arr).replace('NORTH SOUTH', '').replace('EAST WEST', '').replace('SOUTH NORTH', '').replace('WEST EAST', '')
    new_plan = [d for d in str.split(' ') if d] if str else []
    return new_plan if len(new_plan) == len(arr) else othersolution2(new_plan)
    
    
dirReduc = othersolution2

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]), ['WEST'])
    
    def test_2(self):
        self.assertEqual(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]), ["NORTH", "WEST", "SOUTH", "EAST"])

    def test_3(self):
        self.assertEqual(dirReduc(['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']), ['NORTH', 'NORTH'])

    def test_4(self):
        self.assertEqual(dirReduc([]), [])

    def test_5(self):
        self.assertEqual(dirReduc(['EAST', 'NORTH', 'EAST', 'WEST']), ['EAST', 'NORTH'])

    def test_6(self):
        self.assertEqual(dirReduc(['EAST', 'EAST', 'WEST', 'NORTH', 'WEST', 'EAST', 'EAST', 'SOUTH', 'NORTH', 'WEST']), ['EAST', 'NORTH'])

    def test_7(self):
        self.assertEqual(dirReduc(['NORTH', 'EAST', 'NORTH', 'EAST', 'WEST', 'WEST', 'EAST', 'EAST', 'WEST', 'SOUTH']), ['NORTH', 'EAST'])


if __name__ == '__main__':
    unittest.main()