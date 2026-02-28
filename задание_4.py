text = input()

for symbol in text:
    if text.count(symbol) == 3:
        print(symbol)
        break
