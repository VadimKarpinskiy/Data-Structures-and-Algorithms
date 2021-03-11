def counting_sort(arr):
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * n
    for i in range(n):
        count_arr[arr[i]] += 1          # counting how many unique numbers are there in an array
    for i in range(1, n):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        result_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    return result_arr


tab = [3, 4, 1, 0, 5, 0, 3, 1]
print(counting_sort(tab))
