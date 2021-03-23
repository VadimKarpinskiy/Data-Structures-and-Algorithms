# Rozwiązanie dla słów ASCII [a...Z]

def is_anagram(w1, w2, k):            # k is an alphabet range
    count_arr = [0] * k
    n = len(w1)
    for i in range(n):
        count_arr[ord(w1[i]) - ord('A')] += 1
        count_arr[ord(w2[i]) - ord('A')] -= 1
    for i in range(k):
        if count_arr[i] != 0:
            return False
    return True


a = "silent"
b = "listen"
print(is_anagram(a, b, ord('z')-ord('A') + 1))
