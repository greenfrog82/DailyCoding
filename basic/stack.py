class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack1:
    def __init__(self, top=None):
        self.top = top

    def pop(self):
        if not self.top:
            raise ValueError

        item = self.top
        self.top = self.top.next
        return item.data

    def peek(self):
        return self.top.data

    def push(self, data):
        tmp = self.top
        self.top = Node(data)
        self.top.next = tmp

    def empty(self):
        return not self.top


class Stack2:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.stack:
            raise ValueError

        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, data):
        return self.stack.append(data)

    def empty(self):
        return not self.stack


Stack = Stack2


if __name__ == '__main__':
    stack = Stack()

    print(stack.empty())

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.empty())

    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())













