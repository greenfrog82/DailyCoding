import unittest

def mysolution(inputs, result):
    dic = {result-val:val for val in inputs}
    dic = {val:dic.get(val) for val in inputs if dic.get(val)}

    del_candidate_keys = {}
    
    for k,v in dic.items():
        if k != v and dic.get(v) and not del_candidate_keys.get(v):
            del_candidate_keys[v] = v

    for k in del_candidate_keys.keys():
        del dic[k]

    
    



    
    


sum_pairs = mysolution

class Test(unittest.TestCase):
    # def test_1(self):
    #     l1 = [1, 4, 8, 7, 3, 15]
    #     self.assertEqual(sum_pairs(l1, 8) , [1, 7])
    
    # def test_2(self):
    #     l2 = [1, -2, 3, 0, -6, 1]
    #     self.assertEqual(sum_pairs(l2, -6) , [0, -6])

    # def test_3(self):
    #     l3 = [20, -13, 40]
    #     self.assertEqual(sum_pairs(l3, -7) , None)

    # def test_4(self):
    #     l4 = [1, 2, 3, 4, 1, 0]
    #     self.assertEqual(sum_pairs(l4, 2) , [1, 1])

    def test_5(self):
        l5 = [10, 5, 2, 3, 7, 5]
        self.assertEqual(sum_pairs(l5, 10) , [3, 7])        

    # def test_6(self):
    #     l6 = [4, -2, 3, 3, 4]
    #     self.assertEqual(sum_pairs(l6, 8) , [4, 4])

    # def test_7(self):
    #     l7 = [0, 2, 0]
    #     self.assertEqual(sum_pairs(l7, 0) , [0, 0])

    # def test_8(self):
    #     l8 = [5, 9, 13, -3]
    #     self.assertEqual(sum_pairs(l8, 10) , [13, -3])

if __name__ == '__main__':
   unittest.main() 