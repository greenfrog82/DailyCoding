import unittest

def mysolution(num):
    return int(''.join(str(pow(int(i), 2)) for i in str(num)))

def othersolution(num):
    return int(''.join(str(int(i)**2) for i in str(num)))

square_digits = othersolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(square_digits(9119), 811181)


if __name__ == '__main__':
    unittest.main()