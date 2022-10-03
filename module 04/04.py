firstChair = int(input('Введите стоимость первого стула: '))
secondChair = int(input('Введите стоимость второго стула: '))
thirdChair = int(input('Введите стоимость третьего стула: '))
sum = firstChair + secondChair + thirdChair
sale = 0
if sum > 10000:
    sale = sum * 10 / 100
finalSum = sum - sale
print('Финальная цена на три стула:', finalSum)