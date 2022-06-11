def binary_search(list, item):
    L = 0
    H = len(list) - 1
    while L <= H:
        m = (L + H) // 2
        guess = list[m]
        if guess == item:
            return m
        elif guess > item:
            H = m - 1
        else:
            L = m + 1
    return -1

myList = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
print(binary_search(myList, 110))