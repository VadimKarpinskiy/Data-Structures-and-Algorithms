class Node:                                                         # opisuje komórkę słownika
    def __init__(self, value, stan, num):
        self.val = value
        self.stan = stan                                            # 0 - free, 1 - taken, 2 - keep-looking
        self.num = num                                              # liczba wystąpień

class MyDict:
    def __init__(self, N):
        self.size = 4 * N
        self.table = [Node(-1, 0, 0) for _ in range(self.size)]

    def hashing(self, n):
        return (((n*73) % 127) + 23) % self.size

    def find(self, n):              # zwróci indeks elementu
        hash = self.hashing(n)
        while self.table[hash].stan != 0 and self.table[hash].val != n:
            hash += 1
            hash %= self.size
        if self.table[hash].val == n:
            return hash
        return -1

    def add(self, n):
        hash = self.hashing(n)
        while self.table[hash].stan != 0:
            hash += 1
            hash %= self.size
        self.table[hash].val = n
        self.table[hash].stan = 1
        self.table[hash].num += 1

    def erase(self, n):
        index = self.find(n)
        if self.table[index].val != -1:
            self.table[index].val = -1
            self.table[index].stan = 2
            self.table[index].num = 0
