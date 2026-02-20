import keyword as k

def check(name):
    if k.iskeyword(name):
        return False
    return name.isidentifier()

name = str(input('Введите предпологаемое имя: '))

if check(name):
    print(f'{name} - допустимое имя в Python')
else:
    print(f'{name} - недопустимое имя в Python')