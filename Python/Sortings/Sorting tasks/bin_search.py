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


tab = [1, 2, 3, 11, 15, 17, 19, 42, 100, 115]
el = 11
print(bin_search(tab, el))
