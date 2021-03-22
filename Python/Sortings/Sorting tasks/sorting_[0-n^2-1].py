# There are n numbers in range [0, n^2 - 1]. We need to sort them optimally

def base_to_base(num, source_base, target_base):
    res = 0
    i = 0
    while num > 0:
        res += num % target_base * pow(source_base, i)
        num //= target_base
        i += 1
    return res

def radix_sort(arr):
    max_el = max(arr)
    exp = 1
    while max_el/exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, k):
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * 10
    for i in range(n):
        index = arr[i] // k
        count_arr[index % 10] += 1          # counting how many unique numbers are there in an array
    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        index = arr[i] // k
        count_arr[index % 10] -= 1
        result_arr[count_arr[index % 10]] = arr[i]
    for i in range(n):
        arr[i] = result_arr[i]

def sorting(arr, base):
    for i in range(base):   # array length is the same as base according to task, can be changed easily
        arr[i] = base_to_base(arr[i], 10, base)
    radix_sort(arr)
    for i in range(base):
        arr[i] = base_to_base(arr[i], base, 10)


tab = [35, 1, 0, 18, 4, 12]
sorting(tab, len(tab))
print(tab)

