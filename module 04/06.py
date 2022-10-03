firstCube = int(input('Кубик Кости: '))
secondCube = int(input('Кубик владельца: '))
if firstCube >= secondCube:
    print('Сумма:', firstCube - secondCube, '\n' + 'Костя платит', '\n' + 'Игра окончена')
else:
    print('Сумма:', firstCube + secondCube, '\n' + 'Владелец платит', '\n' + 'Игра окончена')
