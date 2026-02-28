text = input()

for letter in text.split():
    if text.count(letter) == 2:
        print(letter)
        break

