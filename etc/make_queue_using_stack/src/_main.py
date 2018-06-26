#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest

if sys.version_info < (3, 0):
  range = xrange
​
# TODO Implement this class.
# Please use follow `Stack` class only.


class Queue(object):
  def __init__(self):
    # TODO implement your codes to here.
    pass


​
# Description
# * Time complexity:
# * Space complexity:
  def enqueue(self, v):
    # TODO implement your codes to here.
    pass
​
# Description
# * Time complexity:
# * Space complexity:
  def dequeue(self):
    # TODO implement your codes to here.
    return 0


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


if __name__ == '__main__':
  unittest.main()    
