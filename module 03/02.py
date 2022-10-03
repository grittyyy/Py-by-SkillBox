firstQuarter = int(input('Сумма за первый квартал: '))
secondQuarter = int(input('Сумма за второй квартал: '))
thirdQuarter = int(input('Сумма за третий квартал: '))
fourthQuarter = int(input('Сумма за четвёртый квартал: '))
sumFirstHalf = firstQuarter + secondQuarter
sumSecondHalf = thirdQuarter + fourthQuarter
print(sumFirstHalf / sumSecondHalf)