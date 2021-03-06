import unittest

def mysolution_1(seq):
    for i, ival in enumerate(seq):
        count = 1
        for j, jval in enumerate(seq):
            if i != j and ival == jval:
                count += 1
        
        if 1 == count % 2:
            return ival

    return None

def mysolution_2(seq):
    from itertools import groupby

    seq.sort()
    for key, group in groupby(seq):
        if 0 != len(list(group)) % 2:
            return key
    return None

def mysolution_3(seq):
    seq.sort()
    cnt = 1
    candidate = seq[0]

    for i in range(1, len(seq)):
        if candidate != seq[i]:
            if 0 != cnt % 2:
                break
            else:
                candidate = seq[i]
                cnt = 1
        else:
            cnt += 1

    return candidate

def other_solution_1(seq):
    for i in seq:
        if seq.count(i)%2 != 0:
            return i

def other_solution_2(seq):
    import operator
    import functools

    return functools.reduce(operator.xor, seq)

def other_solution_3(seq):
    return next(x for x in set(seq) if 1 == seq.count(x) % 2)   
    
# This is my bother's solution 
def solution_ryu(seq):
    return next(s for s in set(seq) if seq.count(s) % 2 != 0)

def solution_ryu2(seq):
    from collections import Counter
    return next(k for k, v in Counter(seq).items() if 0 != v % 2)

        
find_it = solution_ryu2
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)

if __name__ == '__main__':
    unittest.main()