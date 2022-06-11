def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])

if __name__ == "__main__":
    print(sum([10,20,30,40,50]))