import sys
import unittest

if sys.version_info < (3, 0):
    range = xrange


class Queue(object):
    def __init__(self):
       self.en_stack = Stack() 
       self.de_stack = Stack()

    def enqueue(self, v):
        self.en_stack.push(v)

    def dequeue(self):
        if self.en_stack.is_empty():
            return None

        self._swap_stack(self.en_stack, self.de_stack)
        val = self.de_stack.pop()
        self._swap_stack(self.de_stack, self.en_stack)
        return val

    def _swap_stack(self, src_stack, des_stack):
        for i in range(src_stack.size()):
            des_stack.push(src_stack.pop())


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class Test(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_1(self):
        self.queue.enqueue(6)
        self.assertEqual(self.queue.dequeue(), 6)
        self.queue.enqueue(3)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_2(self):
        self.queue.enqueue(45)
        self.queue.enqueue(27)
        self.assertEqual(self.queue.dequeue(), 45)
        self.queue.enqueue(12)
        self.queue.enqueue(28)
        self.queue.enqueue(39)
        self.assertEqual(self.queue.dequeue(), 27)
        self.assertEqual(self.queue.dequeue(), 12)
        self.queue.enqueue(34)
        self.queue.enqueue(12)
        self.queue.enqueue(6)
        self.queue.enqueue(42)
        self.assertEqual(self.queue.dequeue(), 28)
        self.assertEqual(self.queue.dequeue(), 39)
        self.assertEqual(self.queue.dequeue(), 34)
        self.queue.enqueue(25)


if __name__ == '__main__':
    unittest.main()