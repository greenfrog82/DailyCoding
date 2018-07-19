import unittest 

def mysolution(sentence):
    return ' '.join(word if 5 > len(word) else word[::-1] for word in sentence.split(' '))

spin_words = mysolution

class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(spin_words('Welcome'), 'emocleW')
        self.assertEqual(spin_words('Hey fellow warriors'), 'Hey wollef sroirraw')
        self.assertEqual(spin_words('This is a test'), 'This is a test')
        self.assertEqual(spin_words('This is another test'), 'This is rehtona test')

unittest.main()