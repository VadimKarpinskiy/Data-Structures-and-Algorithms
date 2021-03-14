from random import randint, seed


class Node:
    def __init__(self):
        self.next = None
        self.value = None

def qsort(L):
    if L is None:
        return
    if L.next is None:
        return L
    less, eq, great = partition(L)
    """
    print("less:", end=" ")
    printlist(less)
    print("eq:", end=" ")
    printlist(eq)
    print("great:", end=" ")
    printlist(great)
    """
    L = insert_to_end(qsort(less), eq)
    L = insert_to_end(L, qsort(great))
    return L

def partition(head):
    eq = Node()
    less = Node()
    great = Node()
    while head is not None:
        if eq.value is None:
            eq.value = head.value
        elif head.value == eq.value:
            tmp = Node()
            tmp.value = head.value
            tmp.next = eq
            eq = tmp
            tmp = None
        elif head.value > eq.value:
            if great.value is None:
                great.value = head.value
            else:
                tmp = Node()
                tmp.value = head.value
                tmp.next = great
                great = tmp
                tmp = None
        else:
            if less.value is None:
                less.value = head.value
            else:
                tmp = Node()
                tmp.value = head.value
                tmp.next = less
                less = tmp
                tmp = None
        head = head.next
    if less.value is None:
        less = None
    if eq.value is None:
        eq = None
    if great.value is None:
        great = None
    return less, eq, great

def insert_to_end(head,node):
    if head is None and node is not None:
        return node
    if head is None and node is None:
        return None
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next
    if node is None:
        tmp.next = None
    else:
        tmp.next = node
    return head


def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next
  
  
def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next
    
print("OK")

