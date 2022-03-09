def binary_search(some_list, item):
    high = len(some_list)-1
    low = 0
    while low <= high:
        mid = round((low + high)/2)
        guess = some_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
list_2 = [and, baby, cake, dog]
print(binary_search(list_2, cake))



