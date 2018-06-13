import unittest

def mysolution(cat_years, dog_years):
    get_year = lambda years, x, y: (years - x) // y if 24 <= years else years // 15
    return [get_year(cat_years, 16, 4), get_year(dog_years, 14, 5)]
    
owned_cat_and_dog = mysolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(owned_cat_and_dog(15, 15), [1, 1])
    
    def test_2(self):
        self.assertEqual(owned_cat_and_dog(24, 24), [2, 2])

    def test_3(self):
        self.assertEqual(owned_cat_and_dog(56, 64), [10, 10])

    def test_4(self):
        self.assertEqual(owned_cat_and_dog(7, 9), [0, 0])

    def test_5(self):
        self.assertEqual(owned_cat_and_dog(18, 21), [1, 1])


if __name__ == '__main__':
    unittest.main()