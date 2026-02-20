print('Ведущий вводит строку: четырехзначное число с неповторяющимеся цифрами.')
number = str(input())
print('\n' * 25)
turn = 0
guess = str(input())
while True:
    turn += 1
    cows = 0
    bulls = 0
    for i in range(0, 4):
        if guess[i] in number:
            if guess[i] == number[i]:
                bulls += 1
            else:
                cows += 1
    print(f'Быков: {bulls} Коров: {cows}')
    if bulls == 4:
        print('Победа!')
    if turn == 10:
        print('Проигрыш!')
        break
    guess = str(input())