# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
import unittest

def solution(player):
    items = set(player)
    items_len = len(items)
    
    if 1 == items_len or 3 == items_len:
        return 0
    
    dic = {1:3,  2:1, 3:2}

    item = items.pop()
    value = dic[item]
    return player.count(item) if value in items else player.count(dic[value])
        

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1, 1, 3, 3, 1]), 3)

    def test_2(self):
        self.assertEqual(solution([2, 3, 2, 2, 3]), 2)

    def test_3(self):
        self.assertEqual(solution([2,2,2,2,2]), 0)

    def test_4(self):
        self.assertEqual(solution([1,2,3,1,2]), 0)


if __name__ == '__main__':
    unittest.main()


    
    
