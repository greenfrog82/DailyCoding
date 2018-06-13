import unittest

def mysolution(string):
    return string[::-1]

solution = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('world'), 'dlrow')

    def test_2(self):
        self.assertEqual(solution('hello'), 'olleh')

    def test_3(self):
        self.assertEqual(solution(''), '')

    def test_4(self):
        self.assertEqual(solution('h'), 'h')

if __name__ == '__main__':
    unittest.main()