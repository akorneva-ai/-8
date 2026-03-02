def happy(number):
    """
    Check for happy ticket
    :param number: ticket number
    :return: None
    """
    if (len(number) % 2 == 0 and sum(int(x) for x in number[:len(number) // 2])
            == sum(int(x) for x in number[len(number) // 2:])):
        return True
    return False

counter = 1

while True:
    num_ticket = input("Введите номер билета: ")
    
    if happy(num_ticket):
        print(counter)
        break
    else:
        counter += 1
