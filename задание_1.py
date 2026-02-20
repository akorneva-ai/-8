text = input()
count = 0
max_count = 0

for x in text:
    if x == ' ':
        count += 1
    elif count > max_count:
        max_count = count
        count = 0

print(max_count)
