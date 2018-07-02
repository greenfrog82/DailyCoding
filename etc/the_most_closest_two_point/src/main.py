import unittest
import operator

def solution(param):
    param = sorted(param)
    param = [[abs(param[i]-param[j]), param[i], param[j]] for i in range(len(param)-1) for j in range(i, len(param)) if param[i] != param[j]]
    param = sorted(param, key=operator.itemgetter(0))
    return param[0][1::]

    
class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([6, 20, 34, 8, 38, 40]), [6, 8])

    def test_2(self):
        self.assertEqual(solution([20, 16, 10, 45, 30, 28, 47]), [28, 30])
   
   
if __name__ == '__main__':
    unittest.main()