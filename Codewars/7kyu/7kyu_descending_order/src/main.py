import unittest 

def mysolution(num):
    return int(''.join(sorted(str(num), reverse=True)))


Descending_Order = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Descending_Order(0), 0)

    def test_2(self):
        self.assertEqual(Descending_Order(15), 51)
    
    def test_3(self):
        self.assertEqual(Descending_Order(123456789), 987654321)


if __name__ == '__main__':
    unittest.main()