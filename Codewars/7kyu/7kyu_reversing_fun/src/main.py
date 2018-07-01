import unittest

def mysolution(arr):
    ret = []
    f_offset = 0
    b_offset = -1
    for i in xrange(int(round(len(arr)/float(2)))):
        if i == len(arr)/2:
            ret.append(arr[b_offset])
        else:
            ret.append(arr[b_offset])
            b_offset -= 1
            ret.append(arr[f_offset])
            f_offset += 1
    return ''.join(ret)

reverse_fun = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse_fun('012345'), '504132')

    def test_2(self):
        self.assertEqual(reverse_fun('jointhedarkside'), 'ejdoiisnktrhaed')

if __name__ == '__main__':
    unittest.main()
