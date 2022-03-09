def create_array(number):
    new_array = []
    for i in range(-number, number + 1):
        new_array.append(i)
    return new_array
print(create_array(5))

