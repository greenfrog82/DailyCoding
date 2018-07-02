import unittest

def mysolution(inputStr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_vowels = 0
    for vowel in vowels:
        num_vowels += inputStr.count(vowel)
    return num_vowels

def othersolution(inputStr):
    return sum(c in 'aeiou' for c in inputStr)

def othersolution2(inputStr):
    return sum(1 for ch in inputStr if ch in 'aeiou')

getCount = othersolution2

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(getCount('abracadabra'), 5)


if __name__ == '__main__':
    unittest.main()