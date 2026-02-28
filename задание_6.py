text = input()

# .split -> разбивает строку на список слов (по пробелам)
for letter in range(len(text.split())- 1, -1, -1):
    print(text.split()[letter], end=' ')
