#-*-coding:utf-8-*-

import unittest

def get_numerator_denominator(existing_product_name, new_product_name):
    existing_product_name_set = set(existing_product_name.split(' '))
    new_product_name_set = set(new_product_name.split(' '))

    denominator = existing_product_name_set | new_product_name_set
    numerator = existing_product_name_set & new_product_name_set

    return (numerator, denominator)

def jaccard_index(existing_product_name, new_product_name):
    numerator, denominator = get_numerator_denominator(existing_product_name, new_product_name)
    return round(float(len(numerator)) / float(len(denominator)), 4)

def mysolution(existing_product_names, new_product_name):
    ret = (jaccard_index(existing_product_names[0], new_product_name), existing_product_names[0])

    for i in xrange(1, len(existing_product_names)):
        j_idx = jaccard_index(existing_product_names[i], new_product_name)
        if j_idx >= ret[0]:
            ret = (j_idx, existing_product_names[i])

    return ret[1]

def mysolution2(existing_product_names, new_product_name):
    jarccard_indices = ((jaccard_index(existing_product_name, new_product_name), existing_product_name) for existing_product_name in existing_product_names)
    sorted_indices = sorted(jarccard_indices, key=lambda x:x[0])
    return sorted_indices[-1][1]

solution = mysolution

class Test(unittest.TestCase):
    def test_get_numerator_denominator(self):
        numerator, denominator = get_numerator_denominator('에스트라 아토 베리어 크림 영양 보습 스킨케어 200ml', '에스트라 아토 베리어 보습 로션 200ml')
        self.assertEqual((numerator, denominator), ({'에스트라','아토','베리어','보습','200ml'}, {'에스트라','아토','베리어','보습','로션','200ml','크림','영양','스킨케어'}))

    def test_jaccard_index(self):
        self.assertEqual(jaccard_index('에스트라 아토 베리어 크림 영양 보습 스킨케어 200ml', '에스트라 아토 베리어 보습 로션 200ml'), 0.5556)

    def test_solution_1(self):
        existing_product_names = [
            '아토팜 판테놀 로션 200ml', 
            '사노산 베이비 케어 로션 200ml',
            '에스트라 아토 베리어 로션 200ml',
            '일리윤 세라마이드 아토 집중크림 무향 100ml',
            '에스트라 리제덤 RX 듀얼 썬크림 50ml'
        ]

        self.assertEqual(solution(existing_product_names, '에스트라 아토 베리어 보습 로션 200ml'), '에스트라 아토 베리어 로션 200ml')

if __name__ == '__main__':
    unittest.main()