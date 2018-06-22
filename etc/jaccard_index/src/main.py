import unittest

def solution(existing_product_names, new_prduct_name = '에스트라 아토 베리어 보습 로션 200ml'):
    pass
    

class Test(unittest.TestCase):
    def test_1(self):
        existing_product_names = [
            '아토팜 판테놀 로션 200ml', 
            '사노산 베이비 케어 로션 200ml',
            '에스트라 아토 베리어 로션 200ml',
            '일리윤 세라마이드 아토 집중크림 무향 100ml',
            '에스트라 리제덤 RX 듀얼 썬크림 50ml'
        ]

        self.assertEqual(solution(existing_product_names), '에스트라 아토 베리어 로션 200ml')




