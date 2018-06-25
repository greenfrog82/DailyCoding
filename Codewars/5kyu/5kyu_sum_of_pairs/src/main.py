import unittest
import random

def mysolution_for_python3(inputs, result):
    dic = {result-val:val for val in inputs}
    dic = {key:dic.get(key) for key in inputs if None != dic.get(key)}

    if not dic:
        return None

    del_candidate_keys = {}
    
    for k,v in dic.items():
        if k != v and None != dic.get(v) and not del_candidate_keys.get(k):
            del_candidate_keys[v] = v

    for k in del_candidate_keys.keys():
        del dic[k]

    dic_with_distance = {}
    for k, v in dic.items():
        if k == v:
            last_indices = []
            last_idx = -1
            while True:
                try:
                    last_idx = inputs.index(k, last_idx + 1) 
                    last_indices.append(last_idx)
                except ValueError:
                    break
            
            if 2 <= len(last_indices):
                dic_with_distance[k] = (v, last_indices[1] - last_indices[0])
        else:
            dic_with_distance[k] = (v, inputs.index(v) - inputs.index(k))

    ret = sorted(dic_with_distance.items(), key=lambda x: x[1])
    
    return [ret[-1][0], ret[-1][1][0]]

from collections import OrderedDict

def mysolution_for_python2(inputs, result):
    tmpdic = {result-val:val for val in inputs}
    dic = OrderedDict()
    
    for key in inputs:
        if None != tmpdic.get(key):
            dic[key] = tmpdic.get(key)

    if not dic:
        return None

    be_deleted_keys = {}
    for k,v in dic.iteritems():
        if None == be_deleted_keys.get(k) and k != v and None != dic.get(v): 
            be_deleted_keys[v] = k

    for k in be_deleted_keys.iterkeys():
        del dic[k]

    most_closest_distance_pair = [None,[None,None]]
    for k, v in dic.iteritems():
        idx_k = idx_v = -1
        try:
            if k == v:
                for i in xrange(2):
                    if 0 == i:
                        idx_k = inputs.index(k, idx_k+1)
                    else:
                        idx_v = inputs.index(v, idx_k+1)
            else:
                idx_k = inputs.index(k)
                idx_v = inputs.index(v)

            most_closest_distance_pair = most_closest_distance_pair if most_closest_distance_pair[0] is not None and most_closest_distance_pair[0] <= idx_v - idx_k else [idx_v - idx_k, [k, v]]
        except ValueError:
            continue

    return most_closest_distance_pair[1]

sum_pairs = mysolution_for_python2

class Test(unittest.TestCase):
    def test_1(self):
        l1 = [1, 4, 8, 7, 3, 15]
        self.assertEqual(sum_pairs(l1, 8) , [1, 7])
    
    def test_2(self):
        l2 = [1, -2, 3, 0, -6, 1]
        self.assertEqual(sum_pairs(l2, -6) , [0, -6])

    def test_3(self):
        l3 = [20, -13, 40]
        self.assertEqual(sum_pairs(l3, -7) , None)

    def test_4(self):
        l4 = [1, 2, 3, 4, 1, 0]
        self.assertEqual(sum_pairs(l4, 2) , [1, 1])

    def test_5(self):
        l5 = [10, 5, 2, 3, 7, 5]
        self.assertEqual(sum_pairs(l5, 10) , [3, 7])        

    def test_6(self):
        l6 = [4, -2, 3, 3, 4]
        self.assertEqual(sum_pairs(l6, 8) , [4, 4])

    def test_7(self):
        l7 = [0, 2, 0]
        self.assertEqual(sum_pairs(l7, 0) , [0, 0])

    def test_8(self):
        l8 = [5, 9, 13, -3]
        self.assertEqual(sum_pairs(l8, 10) , [13, -3])

    def test_9(self):
        # data = [random.randint(1, 100) for i in range(10000000)]

        # file = open('data.txt', 'w')
        # file.write(','.join(str(i) for i in data))
        # file.close()

        file = open('data.txt', 'r')
        content = file.read().split(',')
        file.close()

        data = [int(i) for i in content]

        sum_pairs(data, 10)
        
if __name__ == '__main__':
   unittest.main() 