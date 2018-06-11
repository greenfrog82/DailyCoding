import unittest

def bonus_time(salary, bonus):
    # return '$%d' % (salary * 10 if bonus else salary)
    return '${}'.format(salary * (10 if bonus else 1))
    

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(bonus_time(10000, True), '$100000')
    
    def test_2(self):
        self.assertEqual(bonus_time(25000, True), '$250000')

    def test_3(self):
        self.assertEqual(bonus_time(10000, False), '$10000')

    def test_4(self):
        self.assertEqual(bonus_time(60000, False), '$60000')

    def test_5(self):
        self.assertEqual(bonus_time(2, True), '$20')

    def test_6(self):
        self.assertEqual(bonus_time(78, False), '$78')

    def test_7(self):
        self.assertEqual(bonus_time(67890, True), '$678900')


if __name__ == '__main__':
    unittest.main()
