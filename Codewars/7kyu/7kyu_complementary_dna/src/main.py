import unittest

def mysolution(dna):
    trans = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join(trans[i] for i in dna)

# This solution only work in python 3.x
def othersolution(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))
    
DNA_strand = othersolution

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(DNA_strand("AAAA"),"TTTT","String AAAA is")

    def test_2(self):
        self.assertEqual(DNA_strand("ATTGC"),"TAACG","String ATTGC is")

    def test_3(self):
        self.assertEqual(DNA_strand("GTAT"),"CATA","String GTAT is")

if __name__ == '__main__':
    unittest.main()