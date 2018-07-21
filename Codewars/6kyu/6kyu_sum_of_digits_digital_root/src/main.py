import unittest

def mysolution(n):
    it = str(n)

    if 1 == len(it):
        return n
    
    return mysolution(sum(int(i) for i in it))

def othersolution(n):
    return n if n < 10 else othersolution(sum(map(int, str(n))))

def othersolution2(n):
    return n%9 or n and 9

digital_root = othersolution2

class Test(unittest.TestCase):
    def test_(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)

unittest.main()