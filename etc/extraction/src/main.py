import unittest

class Node(object):
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node if prev_node else self
        self.next_node = next_node if next_node else self

class CircularLinkedList(object):
    def __init__(self, n):
        self.head = None
        for i in range(1, n+1):
            if None == self.head:
                self.head = Node(i)
            else:
                self.head.prev_node.next_node = Node(i, prev_node=self.head.prev_node, next_node=self.head)
                self.head.prev_node = self.head.prev_node.next_node
                
    def find_by_next(self, base_node, move_cnt):
        if not self.head:
            return None 

        founded_node = base_node
        for _ in range(move_cnt):
            founded_node = founded_node.next_node
        return founded_node

    def find_by_prev(self, base_node, move_cnt):
        if not self.head:
            return None

        founded_node = base_node
        for _ in range(move_cnt):
            founded_node = founded_node.prev_node
        return founded_node

    def remove(self, target_node):
        if not self.head:
            return None
        
        if target_node == self.head:
            self.head = target_node.next_node
            
        target_node.prev_node.next_node = target_node.next_node
        target_node.next_node.prev_node = target_node.prev_node

        return target_node.next_node

    def getlist(self):
        ret = []
        curr_node = self.head
        while(True):
            ret.append(curr_node.data)
            curr_node = curr_node.next_node

            if self.head == curr_node: 
                break

        return ret

def solution(n, d, k, j):
    clist = CircularLinkedList(n)
    
    founded_node = clist.head
    while(clist.head != clist.head.next_node):
        founded_node = clist.find_by_next(founded_node, k) if d else clist.find_by_prev(founded_node, k)
        clist.remove(founded_node)
        k += j

    return clist.head.data

        
class Test(unittest.TestCase):
    def test_clist_1(self):
        clist = CircularLinkedList(5)
        self.assertEqual(clist.getlist(), [1, 2, 3, 4, 5])

    def test_clist_2(self):
        clist = CircularLinkedList(5)

        founded_node = clist.find_by_next(clist.head, 4)
        self.assertEqual(founded_node.data, 5)

        founded_node = clist.find_by_next(clist.head, 6)
        self.assertEqual(founded_node.data, 2)
    
    def test_clist_3(self):
        clist = CircularLinkedList(5)

        founded_node = clist.find_by_prev(clist.head, 4)
        self.assertEqual(founded_node.data, 2)

        founded_node = clist.find_by_prev(clist.head, 6)
        self.assertEqual(founded_node.data, 5)

    def test_clist_4(self):
        clist = CircularLinkedList(5)

        clist.remove(clist.head)
        self.assertEqual(clist.head.data, 2)

        founded_node = clist.find_by_next(clist.head, 1)
        self.assertEqual(founded_node.data, 3)
        
    def test_1(self):
        self.assertEqual(solution(6, 1, 1, 1), 6)

    def test_2(self):
        self.assertEqual(solution(4, 0, 2, 2), 1)

if __name__ == '__main__':
    unittest.main()