money = int(input('Введите сумму, которую хотите снять: '))
if money % 100 != 0:
    print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
else:
    print('Сумма может быть выдана')