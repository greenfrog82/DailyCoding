import unittest
import numbers

def mysolution(array):
    count_with_out_zero = 0

    for i, value in enumerate(array):
        if type(value) is not int and type(value) is not float or 0 != value:
            array[count_with_out_zero] = value
            count_with_out_zero += 1

    for i in range(len(array) - count_with_out_zero):
        array[count_with_out_zero + i] = 0
        
    return array

def mysolution2(array):
   return sorted(array, key=lambda v: 0==v if type(v) is not bool else v)
        
move_zeros = mysolution2

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
    
    def test_2(self):
        self.assertEqual(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])

    def test_3(self):
        self.assertEqual(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])

    def test_4(self):
        self.assertEqual(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])

    def test_5(self):
        self.assertEqual(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])

    def test_6(self):
        self.assertEqual(move_zeros(["a","b"]),["a","b"])

    def test_7(self):
        self.assertEqual(move_zeros(["a"]),["a"])

    def test_8(self):
        self.assertEqual(move_zeros([0,0]),[0,0])

    def test_9(self):
        self.assertEqual(move_zeros([0]),[0])

    def test_10(self):
        self.assertEqual(move_zeros([]),[])


if __name__ == '__main__':
    unittest.main()