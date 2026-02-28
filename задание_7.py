text = input()
length = []

for letter in text.split():
    length.append(len(letter))
    min_lenght = min(length)
print(min_lenght)
