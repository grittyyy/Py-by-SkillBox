item = int(input())
low = 0
high = 100
while True:
    middle = (low + high) // 2
    print(middle)
    print('Угадал?')
    answer = int(input())
    if answer == 1:
        print(middle)
        print('Угадал!!!!!!!!')
        break
    if answer == 2:
        low = middle + 1
    if answer == 3:
        high = middle - 1