print('Ведущий вводит две строки: подсказку и загаданное слово.')
hint = str(input())
word = str(input())
print('\n' * 25)
turn = 0
guess = '*' * len(word)
while True:
    turn += 1
    print(hint)
    print(guess)
    switch = int(input('Буква или слово (0 - буква, 1 - слово)?'))
    if switch == 0:
        bukva = str(input())
        if word.count(bukva) > 0:
            for i in range(len(word)):
                if word[i] == bukva:
                    guess = guess[:i] + bukva + guess[i+1:]
    else:
        wordguess = str(input())
        if wordguess == word:
            print('Победа!')
            break
        else:
            print('Проигрыш!')
    if turn == 10:
        print('Проигрыш!')
        break