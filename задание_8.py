text = input()
length = []

for letter in text.split():
    length.append(len(letter))
    length.sort() #.sort выводит элементы списка в порядке возрастания
print(length)
