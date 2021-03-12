def counting_sort(arr, k):           # [0..k] - k is the upper bound of the interval of possible array elements
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * k
    for i in range(n):
        count_arr[arr[i]] += 1          # counting how many unique numbers are there in an array
    for i in range(1, k):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        result_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
    return result_arr


tab = [17, 33, 2, 0, 42, 2, 777, 322, 5, 15]
k = 1000
print(counting_sort(tab, k))
