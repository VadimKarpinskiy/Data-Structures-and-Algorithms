def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        min_el = A[i]
        for j in range(i, n):
            if arr[j] < min_el:
                min_ind = j
                min_el = arr[j]
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
selection_sort(tab)
print(tab)
