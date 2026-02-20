text = 'Berlin Novgorod Demichev Vologda Anadir Ravioli Ilotsk Kirov Voroneg Go'

turn = 0
words = text.lower().split()
print(len(words))
for i in range(1, len(words)):
    turn += 1
    if words[i][0] == words[i-1][-1]:
        pass
    else:
        turn -= 1
        break
if turn % 2 == 0:
    print('Петя выиграл')
else:
    print('Вася выиграл')
print(turn)