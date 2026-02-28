text = input()

count = 1
max_count = 1

for symbol in range(len(text) - 1):
    if text[symbol] == text[symbol + 1]:
        count += 1
    elif count > max_count:
        max_count = count
        count = 0

print(max_count)
