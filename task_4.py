def first_digit_after_comma(number):
    first_digit = int((number - int(number))*10)
    return first_digit
print(first_digit_after_comma(505.86))
