import unittest

def reverseWords(str):
    # return ' '.join(reversed(str.split(' ')))
    # return ' '.join(reversed(str.split()))
    return ' '.join(str.split(' ')[::-1])


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverseWords("hello world!"), "world! hello")

if __name__ == '__main__':
    unittest.main()
