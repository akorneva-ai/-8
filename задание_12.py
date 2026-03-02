import keyword
name = input()

#keyword -> ключевые слова
# .iskeyword() -> проверяет, не является ли имя зарезервированным
#.isidentifier -> проверяет все правила имен
if not keyword.iskeyword(name) and name.isidentifier():
    print(f"{name} допустимое имя в Python)
else:
    print(f"{name} - недопустимое имя в Python")
