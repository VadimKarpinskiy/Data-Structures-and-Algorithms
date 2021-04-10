class Node:
    def __init__(self):
        self.val = None
        self.next = None

class Stack:
    def __init__(self):
        self.top = Node()  # pointer

    def push(self, x):
        N = Node()
        N.val = x
        N.next = self.top
        self.top.next = N

    def pop(self):
        tmp = self.top.next
        self.top.next = tmp.next
        return tmp.val

    def is_empty(self):
        return self.top.next is None
