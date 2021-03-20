class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


def add_to_end(node, data):
    if node is None:
        return Node(data, None)
    while node.next is not None:
        node = node.next
    node.next = Node(data,None)

def add_to_start(node, data):
    tmp = Node(data)
    tmp.next = node
    return tmp

def reverse(node):
    if node is None:
        return
    head = node
    while node.next is not None:
        tmp = node.next
        node.next = tmp.next
        head = add_to_start(head,tmp.data)
    return head

def list_print(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()


a = Node(5, None)
add_to_end(a, 4)
add_to_end(a, 3)
add_to_end(a, 2)
add_to_end(a, 1)
add_to_end(a, 0)

list_print(a)

a = add_to_start(a, 8)
list_print(a)

a = reverse(a)
list_print(a)
