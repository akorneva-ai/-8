text = 'hahafffffffff text about spaces oo000000hohoh     '

c = 1
k = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        c += 1
        k = max(k, c)
    else:
        c = 1
print(k)