text = 'total growth is 300%'


for k in range(len(text.split()) - 1, -1, -1):
    print(text.split()[k], end=' ')