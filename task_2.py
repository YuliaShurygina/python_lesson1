def find_maximum(some_list):
    if len(some_list) == 0:
        return -1
    maximum = some_list[0]
    for i in range(1, len(some_list)):
        if some_list[i] > maximum:
            maximum = some_list[i]
    return maximum
my_list = [10,6,89,9,12]
print(find_maximum(my_list))