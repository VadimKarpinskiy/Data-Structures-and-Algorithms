import random

def random_partition(arr, p, r):
    ind = random.randint(p, r)
    arr[ind], arr[r] = arr[r], arr[ind]
    return partition(arr, p, r)

def partition(arr, p, r):
    pivot = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def random_select(arr, p, r, i):
    while p < r:
        q = random_partition(arr, p, r)
        k = q-p+1
        if i == k:
            return arr[q]
        if i < k:
            r = q - 1
        else:
            p = q+1
            i -= k
    return arr[p]


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
print(random_select(tab, 0, len(tab)-1, 7))




