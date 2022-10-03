income = int(input('Введите сумму дохода: '))
taxrate = 0
 
if (income > 50000):
    taxrate += (income - 50000) * 30 / 100
    income = 50000
if (income > 10000):
    taxrate += (income - 10000) * 20 / 100
    income = 10000
taxrate += income * 13 / 100
 
print('Сумма налога будет составлять', taxrate)