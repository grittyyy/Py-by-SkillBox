mileage = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
a = mileage // 100
b = (mileage // 10) % 10
c = mileage % 10
if a + b + c > date:
    print('Сброс.')
    mileage = 0
    print('Пробег:', mileage)
else:
    print('Сегодня не сломался.')
    print('Пробег:', mileage)