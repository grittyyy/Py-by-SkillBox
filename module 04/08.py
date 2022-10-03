hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
moneyForFood = int(input('Введите траты на еду: '))
salary = 200 * hours / 2**3 + hours
if (salary >= credit + moneyForFood):
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')