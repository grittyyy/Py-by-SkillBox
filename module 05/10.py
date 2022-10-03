hour = int(input('Введите час в который собираетесь прийти: '))
if hour >= 8 and hour < 22 and hour != 14 and hour != 10 and hour != 11 and hour != 18 and hour != 19:
    print('Можно получить посылку')
else:
    print('Посылку получить нельзя')

#--------------------------------------Второй вариант, где при выполнении условия пишет - посылку получить нельзя

hour = int(input('Введите час в который собираетесь прийти: '))
if not(hour >= 8 and hour < 22 and hour != 14 and hour != 10 and hour != 11 and hour != 18 and hour != 19):
    print('Посылку получить нельзя')
else:
    print('Можно получить посылку')