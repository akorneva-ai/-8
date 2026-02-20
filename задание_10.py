def not_again(word):
    for i in word:
        if word.count(i) == 1:
            pass
        else:
            return False
    return True

text = "easy isn't always easy"

for i in text.split():
    if i != text.split()[0] and not_again(i):
        print(i, end=' ')