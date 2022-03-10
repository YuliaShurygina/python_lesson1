#Найти расстояние между двумя точками пространства
import random
x1 = random.randint(-10,10)
y1 = random.randint(-10,10)
x2 = random.randint(-10,10)
y2 = random.randint(-10,10)
print(x1,y1)
print(x2,y2)
distance  = round(((((x2 - x1)**2) + ((y2 - y1)**2))**0.5), 2)
print(distance)