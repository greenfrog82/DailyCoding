import unittest

def mysolution(n):
    
    ret = []
    tmp = n[::-1]
    for i in xrange(len(n)):
        ret.append(tmp[0])
        tmp = tmp[1::][::-1]
        
    return ''.join(ret)

reverse_fun = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_fun('012345'), '504132')

    def test_2(self):
        self.assertEqual(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')


if __name__ == '__main__':
    unittest.main()