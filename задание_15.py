print('Ведущий вводит строку: четырехзначное число с неповторяющимеся цифрами.')

number = str(input())

print("\n" * 25, "Введите четырёхзначное число: ")

player_input = str(input())
count = 0

while True:
    count += 1
    cows = 0
    bulls = 0

    for digit in range(0, 4):
         if player_input[digit] == number[digit]:
            bulls += 1
         elif player_input[digit] != number[digit] and player_input[digit] in number:
            cows += 1

    print(f'Быков: {bulls} Коров: {cows}')

    if bulls == 4:
        print("Победа!")
        break

    if count > 10:
        print("Проигрыш!")
        break

    player_input = str(input())
