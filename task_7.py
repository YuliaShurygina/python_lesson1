#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
x = True
y = False
z = False
def truth(x,y,z):
    return not(x or y or z) is (not x and not y and not z)
print(truth(x,y,z))