line_1 = input()
line_2 = input()
line_3 = input()

result = []

for symbol in line_1 + line_2 + line_3:
    if line_1.count(symbol) > 0 and (line_2 + line_3).count(symbol) == 0:
        result.append(symbol)
    elif line_2.count(symbol) > 0 and (line_3 + line_1).count(symbol) == 0:
        result.append(symbol)
    elif line_3.count(symbol) > 0 and (line_1 + line_2).count(symbol) == 0:
        result.append(symbol)

#set (множество) - это тип данных 
#для хранения уникальных элементов (без повторений
print(set(result))
