def min_platforms(arrival, departure):
    train = 0           # liczba pociągów
    platforms = 0       # liczba potrzebnych platform

    i = j = 0           # i - czas przybycia, j - czas odjazdu

    while i < len(arrival):
        if arrival[i] < departure[j]:
            train += 1
            platforms = max(platforms, train)
            i += 1
        else:
            train -= 1
            j += 1
    return platforms


arr = [2.00, 2.10, 3.00, 3.20, 3.50, 5.00]
depar = [2.30, 3.40, 3.20, 4.30, 4.00, 5.20]
arr.sort()
depar.sort()
print("Minimum platforms needed is", min_platforms(arr, depar))
