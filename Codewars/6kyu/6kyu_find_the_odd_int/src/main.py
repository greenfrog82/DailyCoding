import unittest

def find_it(seq):
    for i, ival in enumerate(seq):
        count = 1
        for j, jval in enumerate(seq):
            if i != j and ival == jval:
                count += 1
        
        if 1 == count % 2:
            return ival

    return None
             
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

if __name__ == '__main__':
    unittest.main()