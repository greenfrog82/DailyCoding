import unittest

def mysolution(string, x):
    for i in range(x):
        string = string[0:i] + string[i::][::-1] 

    return string

    
    
string_func = mysolution

class Test(unittest.TestCase):
    # def test_1(self):
    #     self.assertEqual(string_func('String', 3), 'nrtgSi')

    def test_2(self):
        self.assertEqual(string_func("This is a string exemplification!",0),"This is a string exemplification!")

    def test_3(self):
        self.assertEqual(string_func("String for test: incommensurability",1),"ySttirliinbga rfuosrn etmemsotc:n i")
    
    def test_4(self):
        self.assertEqual(string_func("Ohh Man God Damn",7)," nGOnmohaadhMD  ")
    
    def test_5(self):
        self.ssertEqual(string_func("Ohh Man God Damnn",19),"haG mnad MhO noDn")        


if __name__ == '__main__':
    unittest.main()