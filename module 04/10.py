a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

max = a
if b > max:
    max = b
if c > max:
    max = c
print('Наибольшее число -', max)