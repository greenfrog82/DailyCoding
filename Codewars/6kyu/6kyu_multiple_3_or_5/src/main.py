import unittest

def mysolution(number):
    return sum(i for i in range(number) if not i % 3 or not i % 5)

solution = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(10), 23)


if __name__ == '__main__':
    unittest.main()
