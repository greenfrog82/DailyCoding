import unittest

def mysolution(str):
    str_len = len(str)
    center_offset = str_len // 2 - 1
    return str[center_offset+1] if str_len % 2 else str[center_offset:center_offset+2]

def other_solution_1(str):
    return str[(len(str)-1)//2:len(str)//2+1]

def other_solution_2(str):
    index, odd = divmod(len(str), 2)
    return str[index] if odd else str[index-1:index+1]

get_middle = other_solution_2

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(get_middle("test"), "es")

    def test_2(self):
        self.assertEqual(get_middle("testing"), "t")

    def test_3(self):
        self.assertEqual(get_middle("middle"), "dd")

    def test_4(self):
        self.assertEqual(get_middle("A"), "A")

    def test_5(self):
        self.assertEqual(get_middle("of"), "of")

if __name__ == '__main__':
    unittest.main()
    
