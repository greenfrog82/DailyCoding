# https://www.codewars.com/kata/5bb50eb68f8bbdb4b300021d/train/python
from collections import Counter

# def solution_1(arg):
def perform(param):
    res = []
    cnt = Counter(param)
        
    while(cnt):
        res.extend([k for k in cnt.keys()])
        cnt -= Counter(cnt.keys())
    
    return res
    
    
def test_case():
    input_ = ["one", "one", "two", "two", "three", "three", "four", "one"]
    output = ["one", "two", "three", "four", "one", "two", "three", "one"]

    assert perform(input_) == output