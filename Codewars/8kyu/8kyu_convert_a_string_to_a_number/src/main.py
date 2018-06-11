import unittest

def string_to_number(s):
    return int(s)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(string_to_number("1234"), 1234)

    def test_2(self):
        self.assertEqual(string_to_number("605"), 605)

    def test_3(self):
        self.assertEqual(string_to_number("1405"), 1405)

    def test_4(self):
        self.assertEqual(string_to_number("1234"), 1234)

    
if __name__ == '__main__':
    unittest.main()
