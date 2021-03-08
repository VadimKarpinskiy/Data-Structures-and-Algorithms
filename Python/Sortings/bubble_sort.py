def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        array_changed = False
        for j in range(n-i-1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                array_changed = True
        if not array_changed:
            return


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
bubble_sort(tab)
print(tab)
