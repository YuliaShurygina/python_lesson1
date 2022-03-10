#Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти
#coordinates = ['x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x > 0, y < 0']
#quater = int(input('Укажите номер четверти от 1 до 4: '))
#print(coordinates[quater - 1])
def coordinates(number):
    if number == 1:
        return 'x > 0 and y > 0 '
    if number == 2:
        return 'x < 0 and y > 0'
    if number == 3:
        return 'x < 0 and y < 0 '
    if number == 4:
        return 'x > 0 and y < 0'
quater = int(input('Укажите номер четверти от 1 до 4: '))
print(coordinates(quater))