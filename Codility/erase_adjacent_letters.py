# https://app.codility.com/tickets/tryDSW53C-UBX/share/8017af9701e2a31c2d9467531f27949ba7413e7781bebafac7f14ac25b045807/#
# EraseAdjacentLetters


def solution(sentence):
    keywords = {'A':'B', 'B':'A', 'C':'D', 'D':'C'}
    tmp = []

    for c in sentence:
        if tmp and tmp[-1] == keywords[c]:
            tmp.pop()
        else:
            tmp.append(c)

    return ''.join(tmp)


def test_cbacd():
    assert solution('CBACD') == 'C'


def test_cababd():
    assert solution('CABABD') == ''
