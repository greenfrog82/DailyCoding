import unittest

def solution(num):
    def to_revsred_num(value):
        return int(str(value)[::-1])
   
    def is_palindrome(value):
        return value == to_revsred_num(value)

    for _ in range(3):
        num += to_revsred_num(num)
        if is_palindrome(num):
            break

    return num if is_palindrome(num) and 10000 > num else -1


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution(57), 363)

    def test_2(self):
        self.assertEqual(solution(78), -1)

    def test_3(self):
        self.assertEqual(solution(85), 484)

    def test_4(self):
        self.assertEqual(solution(196), -1)


if __name__ == '__main__':
    unittest.main()