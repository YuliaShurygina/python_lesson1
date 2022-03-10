#Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
def weekend(some_number):
    return some_number==5 or some_number==6
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
number = int(input('Введите число, обозначающее день недели от 0 до 6: '))
if weekend(number) == True:
    print(weekdays[number], '- выходной!')
else:
    print(weekdays[number], '- не является выходным днем.')


