import unittest

def fake_bin(x):
    # return ''.join('0' if 5 > int(ch) else '1' for ch in x)
    return ''.join('0' if '5' > ch else '1' for ch in x)


class Test(unittest.TestCase):
    def test_1(self):
        tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]

        for exp, inp in tests:
            self.assertEqual(fake_bin(inp), exp)


if __name__ == '__main__':
    unittest.main()