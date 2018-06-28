import unittest

# my solution
# def common(num, op):
#     return op(num) if op is not None else num    

# def zero(op = None):
#     return common(0, op)
# def one(op = None):
#     return common(1, op)
# def two(op = None):
#     return common(2, op)
# def three(op = None):
#     return common(3, op)
# def four(op = None):
#     return common(4, op)
# def five(op = None):
#     return common(5, op)
# def six(op = None):
#     return common(6, op)
# def seven(op = None):
#     return common(7, op)
# def eight(op = None):
#     return common(8, op)
# def nine(op = None):
#     return common(9, op)

# def plus(n): 
#     return lambda x: x + n
# def minus(n):
#     return lambda x: x - n
# def times(n):
#     return lambda x: x * n
# def divided_by(n):
#     return lambda x: x // n

# other solution

zero, one, two, three, four, five, six, seven, eight, nine = (lambda op=None: op(i) if op is not None else i for i in range(10))

plus = lambda y: lambda x: x+y
minus = lambda y: lambda x: x-y
times = lambda y: lambda x: x*y
divided_by = lambda y: lambda x: x//y


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(seven(times(five())), 35)

    def test_2(self):
        self.assertEqual(four(plus(nine())), 13)

    def test_3(self):
        self.assertEqual(eight(minus(three())), 5)

    def test_4(self):
        self.assertEqual(six(divided_by(two())), 3)

if __name__ == '__main__':
    unittest.main()