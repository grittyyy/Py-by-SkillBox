first, second, third = int(input('Введите первое число: ')), int(input('Введите первое число: ')), int(input('Введите первое число: '))
if first == second or second == third:
    if second == third and first == second:
        print(3)
    else:
        print(2)
elif first == third:
    print(2)
else:
    print(0)
