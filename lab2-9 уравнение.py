# Вариант №1
x = int(input('Введите x: '))
y = 1 / ((1 - (x**4) - (x**2))**0.5)
if (1 - (x**4) - (x**2)) > 0:
    print('y =', y)
else:
    print('Нет решений')
