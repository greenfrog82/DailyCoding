import unittest
import random

# Returns number of pairs in arr[0..n-1] 
# with sum equal to 'sum'
def getPairsCount(arr, n, sum):
     
    m = [0] * n
     
    # Store counts of all elements in map m
    for i in range(0, n):
        # m[arr[i]]
        m[arr[i]] += 1
 
    twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is 
    # counted twice)
    for i in range(0, n):
     
        twice_count += m[sum - arr[i]] 
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such 
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
     
    # return the half of twice_count
    return int(twice_count / 2) 

class Test(unittest.TestCase):
        def test_1(self):
           arr = [random.randint(1, 1000) for i in range(10000000)] 
           print(getPairsCount(arr, len(arr), 10))

           

if __name__ == '__main__':
        unittest.main()