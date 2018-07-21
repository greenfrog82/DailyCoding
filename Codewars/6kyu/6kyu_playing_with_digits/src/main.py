import unittest

def mysolution(n, p):
    ret_sum = 0
    for i in str(n):
        ret_sum += int(i) ** p
        p += 1

    return ret_sum / n if 0 == ret_sum % n else -1

def othersolution(n, p):
    ss = 0
    for i, v in enumerate(str(n)):
        ss += int(v)**(p+i)
    return ss/n if 0==ss%n else -1
        
        
dig_pow = othersolution

class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)

unittest.main()