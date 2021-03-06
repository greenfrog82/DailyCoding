import unittest

def get_moving_indexes(inputs):
    cnt = len(inputs[0])

    repeat_count = [cnt-1, cnt-1, cnt-1, cnt-2]
    moving_index = [0]

    idx = 0
    for i, repeat in enumerate(repeat_count):
        if 0 == i:
            op = 1
        elif 1 == i:
            op = cnt
        elif 2 == i:
            op = -1
        else:
            op = -cnt

        for _ in range(repeat):
            idx += op
            moving_index.append(idx)

    return moving_index

def solution(inputs, k):
    moving_indexes = get_moving_indexes(inputs)
    converted_inputs = [j for i in range(len(inputs)) for j in inputs[i]]
    cnt = len(moving_indexes)

    tmp_ret = [i for i in converted_inputs]
    for i, src_idx in enumerate(moving_indexes):
        moving_idx = i + k
        if moving_idx >= cnt:
            moving_idx -= cnt
        
        dest_idx = moving_indexes[moving_idx]
        tmp_ret[dest_idx] = converted_inputs[src_idx]
        
    ret = []
    tmp = []
    for i, item in enumerate(tmp_ret):
        tmp.append(item)
        if 0 == (i+1) % len(inputs[0]):
            ret.append(tmp)
            tmp = []

    return ret

def report(inputs, num):
    ret = solution(inputs, num)
    return '[%s]' % ','.join('[%s]' % ','.join(str(item) for item in arr) for arr in ret)
     
    
class Test(unittest.TestCase):
    def test_get_moving_indexes_1(self):
        self.assertEqual(get_moving_indexes([[1,2,3],[5,6,7],[9,10,11]]), [0, 1, 2, 5, 8, 7, 6, 3])

    def test_get_moving_indexes_2(self):
        self.assertEqual(get_moving_indexes([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4])

    def test_solution_1(self):
        self.assertEqual(solution([[1,2,3],[5,6,7],[9,10,11]], 3), [[10,9,5],[11,6,1],[7,3,2]])

    def test_solution_2(self):
        self.assertEqual(solution([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],2 ), [[9,5,1,2],[13,6,7,3],[14,10,11,4],[15,16,12,8]])


if __name__ == '__main__':
    unittest.main()

