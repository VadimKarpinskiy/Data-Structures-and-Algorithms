# We can find both min and max element in less than (2n-2) operations, where n - the length of array.
# The idea is to compare two elements of an array, and then compare the greatest one with our current max element,
# and the smaller one with our current min element. That means we will have 3 comparisons for each 2 elements
# instead of 2 comparisons for each element

def min_max_find(arr):
    n = len(arr)
    if n == 0:
        return
    min_el = arr[0]
    max_el = arr[0]
    i = 1
    while i < (n-1):
        if arr[i] <= arr[i+1]:
            if arr[i] < min_el:
                min_el = arr[i]
            if arr[i+1] > max_el:
                max_el = arr[i+1]
        else:
            if arr[i+1] < min_el:
                min_el = arr[i+1]
            if arr[i] > max_el:
                max_el = arr[i]
        i += 2
    if n % 2 == 0:              # the last element will be unchecked if the array length is even
        if arr[i] > max_el:
            max_el = arr[i]
        elif arr[i] < min_el:
            min_el = arr[i]
    return min_el, max_el


# testing different cases:
tab1 = []
tab2 = [1]
tab3 = [1, 2]
tab4 = [9, 1, 1]
tab5 = [33, 18, -1, 100]

print(min_max_find(tab1))
print(min_max_find(tab2))
print(min_max_find(tab3))
print(min_max_find(tab4))
print(min_max_find(tab5))


