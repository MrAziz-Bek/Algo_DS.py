def find_max(array):
    max = array[0]
    max_index = 0
    for i in range(1, len(array)):
        if max < array[i]:
            max = array[i]
            max_index = i
    return max_index

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        max_index = find_max(array)
        new_array.append(array.pop(max_index))
    return new_array

array = [3, 4, 1, 6, 10, 20, 9, 8]
print(selection_sort(array))