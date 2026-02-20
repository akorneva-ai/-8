def happy(number):
    if sum(int(x) for x in number[:len(number) // 2]) == sum(int(x) for x in number[len(number) // 2:]):
        return True
    return False


order = 0
while True:
    order += 1
    number = str(input('Номер билета: '))
    if len(number) % 2 == 0:
        if happy(number):
            print(order)
            break