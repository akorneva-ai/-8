text = input()

count = 0
result = []

# .count() ->
# -> кол-во определённого элемента в тексте

for letter in text:
    if letter not in result:
        result.append(letter)
        count += 1
print(count)
