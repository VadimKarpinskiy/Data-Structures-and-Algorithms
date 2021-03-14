class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


def delete_max(head):
    if head.value is None or head.next is None:
        return None
    tmp = head
    max_node = head
    holder = head
    while tmp.next is not None:
        if tmp.next.value > max_node.value:
            holder = tmp
            tmp = tmp.next
            max_node = tmp
        else:
            tmp = tmp.next
    if max_node.value == head.value:        # case: 5 -> 4 -> 3 -> 2 -> 1 -> None
        return head.next
    holder.next = max_node.next
    return head

def print_list(head):
    while head is not None:
        print(head.value)
        head = head.next


a = Node(10)
b = Node(5)
c = Node(3)
a.next = b
b.next = c
c.next = None
a = delete_max(a)
print_list(a)
