def search_minimum(array):
    minimum = array[0]
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < minimum:
            minimum = array[i]
            min_index = i
    return min_index
def sort_array(arr):
    new_array = []
    for i in range(len(arr)):
        minimum_index = search_minimum(arr)
        new_array.append(arr.pop(minimum_index))
    return new_array
print(sort_array([5, 3, 6, 2, 10]))
#print(search_minimum([5,3,6, 2, 10]))