class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse(node):
    res = None
    while node is not None:
        res = add_to_start(res, node.data)
        node = node.next
    return res

def add_to_start(node, data):
    tmp = Node(data)
    tmp.next = node
    return tmp

def list_print(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


# Testing
a = Node(5, None)
a = add_to_start(a, 4)
a = add_to_start(a, 3)
a = add_to_start(a, 2)
a = add_to_start(a, 1)
a = add_to_start(a, 0)

list_print(a)
list_print(reverse(a))

b = None
list_print(reverse(b))
