import unittest

def to_alternating_case(string):
    # return ''.join(ch if not ch.isalpha() else ch.upper() if ch.islower() else ch.lower() for ch in string)
    # return string.swapcase()
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in string)
    


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(to_alternating_case("hello world"), "HELLO WORLD")

    def test_2(self):
        self.assertEqual(to_alternating_case("HELLO WORLD"), "hello world")

    def test_3(self):
        self.assertEqual(to_alternating_case("hello WORLD"), "HELLO world")

    def test_4(self):
        self.assertEqual(to_alternating_case("HeLLo WoRLD"), "hEllO wOrld")

    def test_5(self):
        self.assertEqual(to_alternating_case("12345"), "12345")

    def test_6(self):
        self.assertEqual(to_alternating_case("1a2b3c4d5e"), "1A2B3C4D5E")

    def test_7(self):
        self.assertEqual(to_alternating_case("String.prototype.toAlternatingCase"), "sTRING.PROTOTYPE.TOaLTERNATINGcASE")

if __name__ == '__main__':
    unittest.main()