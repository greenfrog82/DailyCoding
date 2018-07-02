import unittest

def mysolution(string):
    return string.translate(str.maketrans('aeiou', ''))
    
disemvowel = mysolution


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")

if __name__ == '__main__':
    unittest.main()