import unittest

def mysolution(n):
    length = len(n)
    n = [n[i] for i in xrange(length-1, -1, -1)]
    
    for i in xrange(1, length-1):
        for j in xrange((length-i)//2):
            n[i+j], n[-(j+1)] = n[-(j+1)], n[i+j]
    return ''.join(n)
            
reverse_fun = mysolution


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_fun('012345'), '504132')

    def test_2(self):
        self.assertEqual(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')

if __name__ == '__main__':
    unittest.main()