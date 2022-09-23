a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
b += a 
a = b - a 
b -= a
print(a, b)