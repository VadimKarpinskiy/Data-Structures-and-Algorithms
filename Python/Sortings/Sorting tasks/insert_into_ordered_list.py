class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

def insert(head, data):
    x = Node(data)
    x.next = None
    if head.value is None:
        return x
    if head.value > x.value:
        x.next = head
        return x
    tmp = head
    while tmp.next is not None and tmp.next.value < x.value:
        tmp = tmp.next
    if tmp.next is None:
        tmp.next = x
    else:
        x.next = tmp.next
        tmp.next = x
    return head

def show(node):
    while node is not None:
        print(node.value)
        node = node.next


a = Node(1)
b = Node(5)
c = Node(6)
a.next = b
b.next = c
c.next = None
a = insert(a, 7)
a = insert(a, 0)
a = insert(a, 2)
show(a)

