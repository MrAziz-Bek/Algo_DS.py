from random import randrange


def qsort(array):
    if len(array) < 2:
        return array
    pivot = array.pop(randrange(len(array)))
    smalls = [i for i in array if i <= pivot]
    bigs = [i for i in array if i > pivot]
    return qsort(smalls) + [pivot] + qsort(bigs)

if __name__ == "__main__":
    print(qsort([5, 12, 1, 0, 66, -5]))