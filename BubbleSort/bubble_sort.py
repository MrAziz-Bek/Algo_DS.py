def bsort(array):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

if __name__ == "__main__":
    print(bsort([5, 2, 8, 0, -4, 7, -1]))