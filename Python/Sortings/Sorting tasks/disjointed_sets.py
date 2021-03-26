# There are two sets of numbers, represented as size arrays of m and n, where
# m is significantly less than n. Suggest an algorithm that will check if the sets are disjointed.

# Algorithm: We sort a small array and then we search every element
# of a big array in a small array, using binary search.
# Complexity: O(m*log(m)) + O(n*log(m)) = O((m+n)*log(m))

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

def bin_search(arr, x):
    p = 0
    r = len(arr) - 1
    while r >= p:
        mid = (p+r)//2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            r = mid - 1
        else:
            p = mid + 1
    return False

def are_disjointed(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    quick_sort(arr1, 0, m-1)
    for i in range(n):
        if bin_search(arr1, arr2[i]):
            return False
    return True


tab1 = [3, 8, 1, 11, 51]
tab2 = [100, 15, 62, 89, 5, 15]
print(are_disjointed(tab1, tab2))



