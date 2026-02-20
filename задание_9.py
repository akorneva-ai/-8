text = "easy isn't always easy"

for i in text.split():
    if text.count(i) == 2:
        print(i)
        break
