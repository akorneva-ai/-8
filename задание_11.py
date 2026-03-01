city = input()

turn = 0 #кол-во пар городов
towns = city.lower().split()

for word in range(1, len(towns)):
    turn += 1
    if towns[word][0] == towns[word - 1][-1]:
        pass
    else:
        turn -= 1
        break
if turn % 2 == 0:
    print('Петя выиграл')
else:
    print('Вася выиграл')
