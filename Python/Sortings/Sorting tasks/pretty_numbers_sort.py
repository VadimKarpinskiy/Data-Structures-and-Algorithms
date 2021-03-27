# A single digit appears in a number only once. A multiple digit is one that appears in a number more than once.
# We say that the natural number A is "prettier" than the natural number B, if it has more single digits.
# In case, when both numbers have the same amount of single digits, a number with fewer multiple digits is prettier.
# For example, 123 is prettier than 455; 1266 is prettier than 114577; 2344 and 67333 are equally pretty.

# Given an array of length n, sort it`s elements from the prettiest to the least-pretty.

# Algorithm: We count how many single and multiple digits are there is a number and create
# tuples/lists like: [number, singles, multiples]. Now the key is to use radix sort firstly to sort an
# array decreasingly on multiple digits, then decreasingly on single digits.
#
# Complexity: O(2d(n+k))
#
def pretty_numbers_sort(arr):
    n = len(arr)
    for i in range(n):
        both = single_multiple_count(arr[i])
        sin = both[0]
        mul = both[1]
        arr[i] = [arr[i], sin, mul]
    radix_sort(arr, 2)
    arr.reverse()               # reverse an array to simulate decreasing radix sort
    radix_sort(arr, 1)

def single_multiple_count(num):
    count_arr = [0]*10
    single = 0
    multiple = 0
    while num != 0:
        count_arr[num % 10] += 1
        num //= 10
    for i in range(len(count_arr)):
        if count_arr[i] == 1:
            single += 1
        elif count_arr[i] > 1:
            multiple += 1
        else:
            continue
    return single, multiple

#0-3 1-7 1-6 2-5 9-1

def radix_sort(arr, round):     # in the first "round" we want to sort an array by multiple numbers and in the
    max_el = arr[0][round]     # second "round" we will sort them by single numbers
    for i in range(len(arr)):
        if arr[i][round] > max_el:
            max_el = arr[i][round]
    exp = 1
    while max_el/exp > 0:
        counting_sort(arr, exp, round)         # radix sort requires some stable sorting algorithm to work properly
        exp *= 10


def counting_sort(arr, k, round):
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * 10
    for i in range(n):
        index = arr[i][round] // k
        count_arr[index % 10] += 1          # counting how many unique numbers are there in an array
    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        index = arr[i][round] // k
        count_arr[index % 10] -= 1
        result_arr[count_arr[index % 10]] = arr[i]
    for i in range(n):
        arr[i] = result_arr[i]


tab = [123, 11, 1234567890, 5113422, 233, 322, 117, 3223, 6, 181]
pretty_numbers_sort(tab)
for i in range(len(tab)):
    tab[i] = tab[i][0]
tab.reverse()                   # reverse an array to simulate decreasing radix sort
print(tab)





