# Using random pivot of an array theoretically should protect our QuickSort algorithm complexity from goinng quadratic.
# However, McILROY in his "A Killer Adversary for Quicksort" described a method that can almost always create
# for which QuickSort`s complexity will be O(n^2). 

import random

def quick_sort(arr, p, r):
    if p < r:
        m = partition(arr, p, r)
        quick_sort(arr, p, m - 1)
        quick_sort(arr, m, r)

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


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
quick_sort(tab, 0, len(tab)-1)
print(tab)
