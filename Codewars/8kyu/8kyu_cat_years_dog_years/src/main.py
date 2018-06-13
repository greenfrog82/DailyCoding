import unittest

def mysolution(human_years):
    cat_years = dog_years = 15
    for year in range(1, human_years):
        if 2 == year + 1:
            cat_years = dog_years = dog_years + 9
        else:
            cat_years += 4
            dog_years += 5

    return [human_years, cat_years, dog_years]

def other_solution_1(x):
    return [x, 24 + ((x-2) * 4) if 1 != x else 15, 24 + ((x-2) * 5) if 1 != x else 15]

def other_solution_2(hy):
    return [hy, 16 + hy * 4, 14 + hy * 5] if hy > 1 else [hy, 15, 15]

def other_solution_3(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]

human_years_cat_years_dog_years = other_solution_3

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(human_years_cat_years_dog_years(1), [1, 15, 15])
    
    def test_2(self):
        self.assertEqual(human_years_cat_years_dog_years(2), [2, 24, 24])

    def test_3(self):
        self.assertEqual(human_years_cat_years_dog_years(10), [10, 56, 64])

if __name__ == '__main__':
    unittest.main()
