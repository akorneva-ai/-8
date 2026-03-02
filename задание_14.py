print("Ведущий вводит две строки: подсказку и загаданное слово.")

hint = input()
hiden_word = str(input())
guess = len(hiden_word) * "*"

print("\n" * 25)
print(hint, "\n", guess, "\n",
      "Буква или слово (0 - буква, 1 - слово)?")

player_input = int(input())
count = 0

while True:
    if player_input == 0:
        letter = input()
        found = False
        count += 1

        for l in range(len(hiden_word)):
            if count <= 10:
                if hiden_word[l] == letter:
                    guess = guess[:l] + letter + guess[l + 1:]
                    found = True
                else:
                    found = False

    if count > 10:
        print("Проигрыш!")
        break

    print(guess, "\n", "Буква или слово (0 - буква, 1 - слово)?")
    player_input = int(input())

    if player_input == 1:
        word = input()
        if count <= 10:
            if word == hiden_word:
                print("Победа!")
            else:
                print("Проигрыш!")
        else:
            print("Проигрыш!")

    break
