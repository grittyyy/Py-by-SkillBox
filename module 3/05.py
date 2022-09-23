minutes = int(input('Введите количество минут: '))
hours = minutes // 60
restMinutes = minutes % 60
print('В часах это:', hours)
print('Остаток минут:', restMinutes)