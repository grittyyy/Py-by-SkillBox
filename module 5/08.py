money, s = int(input('Введите стоимость квартиры: ')), int(input('Введите площадь квартиры: '))
if (money <= 10000000 and s >= 100) or (money <= 7000000 and s >= 80):
    print('Эту квартиру можно брать')
else:
    print('Эту квартиру не стоит брать')
