import unittest

MORSE_CODE = {
    '.-': 'A', 
    '-....': 'B',
    '-.-.': 'C', 
    '-..': 'D',
    '.': 'E',
    '..-.' : 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--...': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '...---...': 'SOS', 
    '.-...': '&', 
    '--..--': ',', 
    '..--..': '?',
    '-...-': '=',
    '.-.-.-': '.',
    '.----.': "'",
    '-.-.-.': ';',
    '-....-': '-', 
    '..--.-': '_', 
    '-.--.-': ')', 
    '-.-.--': '!',
    '-..-.': '/', 
    '.-.-.': '+', 
    '---...': ':',
    '.--.-.': '@', 
    '...-..-': '$',
    '.-..-.': '"', 
    '-.--.': '(',
}

def mysolution(morse_code):
    splited_morse_codes = morse_code.strip().replace('   ', '  ').split(' ')
    return ''.join(MORSE_CODE[code] if code else ' ' for code in splited_morse_codes)

def another_solution(morse_code):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))
    
decodeMorse = another_solution 

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')

    def test_2(self):
        self.assertEqual(decodeMorse(' . '), 'E')


if __name__ == '__main__':
    unittest.main()