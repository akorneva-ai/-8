text = input()

words = text.split()
first_word = words[0]
result = []

def not_repeat(word):
    for letter in word:
        if word.count(letter) > 1:
            return True
    return False

for word in words:
    if not not_repeat(word) and word != first_word:
        result.append(word)
print(result)
