import unittest

def mysolution(str):
    str = str.lower()
    return str.count('x') == str.count('o')

xo = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(xo('xo'), 'True expected')
        self.assertTrue(xo('xo0'), 'True expected')
        self.assertTrue(not xo('xxxoo'), 'False expected')
        self.assertTrue(xo('xXXXOOoo'))

if __name__ == '__main__':
    unittest.main()