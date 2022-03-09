def check_ratio(number):
    if number%30 == 0:
        return False
    return  number % 5 == 0 and number % 10 == 0 or number % 15 == 0
print(check_ratio(515))
