def number_to_russian(n):
    """
    Преобразует натуральное число (не превосходящее 900 000 000) в русские слова.

    Args:
        n: Натуральное число.

    Returns:
        Строка, представляющая число русскими словами.
    """

    if n == 0:
        return "ноль"

    def get_hundreds(num):
        hundreds = num // 100
        tens = (num % 100) // 10
        units = num % 10

        hundreds_str = ""
        if hundreds > 0:
            if hundreds == 1:
                hundreds_str = "сто"
            elif hundreds == 2:
                hundreds_str = "двести"
            elif hundreds == 3:
                hundreds_str = "триста"
            elif hundreds == 4:
                hundreds_str = "четыреста"
            elif hundreds == 5:
                hundreds_str = "пятьсот"
            elif hundreds == 6:
                hundreds_str = "шестьсот"
            elif hundreds == 7:
                hundreds_str = "семьсот"
            elif hundreds == 8:
                hundreds_str = "восемьсот"
            elif hundreds == 9:
                hundreds_str = "девятьсот"

        tens_str = ""
        if tens == 1:
            if units == 0:
                tens_str = "десять"
            elif units == 1:
                tens_str = "одиннадцать"
            elif units == 2:
                tens_str = "двенадцать"
            elif units == 3:
                tens_str = "тринадцать"
            elif units == 4:
                tens_str = "четырнадцать"
            elif units == 5:
                tens_str = "пятнадцать"
            elif units == 6:
                tens_str = "шестнадцать"
            elif units == 7:
                tens_str = "семнадцать"
            elif units == 8:
                tens_str = "восемнадцать"
            elif units == 9:
                tens_str = "девятнадцать"
        elif tens == 2:
            tens_str = "двадцать"
        elif tens == 3:
            tens_str = "тридцать"
        elif tens == 4:
            tens_str = "сорок"
        elif tens == 5:
            tens_str = "пятьдесят"
        elif tens == 6:
            tens_str = "шестьдесят"
        elif tens == 7:
            tens_str = "семьдесят"
        elif tens == 8:
            tens_str = "восемьдесят"
        elif tens == 9:
            tens_str = "девяносто"

        units_str = ""
        if units == 1:
            units_str = "один"
        elif units == 2:
            units_str = "два"
        elif units == 3:
            units_str = "три"
        elif units == 4:
            units_str = "четыре"
        elif units == 5:
            units_str = "пять"
        elif units == 6:
            units_str = "шесть"
        elif units == 7:
            units_str = "семь"
        elif units == 8:
            units_str = "восемь"
        elif units == 9:
            units_str = "девять"

        result = ""
        if hundreds_str:
            result += hundreds_str + " "
        if tens_str:
            result += tens_str + " "
        if units_str:
            result += units_str
        return result.strip()

    if n < 1000:
        return get_hundreds(n)
    elif n < 1000000:
        thousands = n // 1000
        remainder = n % 1000
        if thousands == 1:
            return "одна тысяча " + get_hundreds(remainder)
        elif 2 <= thousands <= 4:
            return f"{thousands} тысячи " + get_hundreds(remainder)
        else:
            return f"{get_hundreds(thousands)} тысяч " + get_hundreds(remainder)
    else:
        millions = n // 1000000
        remainder = n % 1000000
        if millions == 1:
            return "один миллион " + (get_hundreds(remainder) if remainder > 0 else "")
        else:
            return f"{get_hundreds(millions)} миллионов " + (get_hundreds(remainder) if remainder > 0 else "")


# Пример использования
number = 120
russian_representation = number_to_russian(number)
print(russian_representation)  # Вывод: сто двадцать три миллиона четыреста пятьдесят шесть тысяч семьсот восемьдесят девять
# Don't work properly