from cmath import inf
from distutils.log import info


russianLang = int(input('Введите количество баллов по русскому языку: '))
math = int(input('Введите количество баллов по математике: '))
informatics = int(input('Введите количество баллов по информатике: '))
sum = russianLang + math + informatics
if sum >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')
