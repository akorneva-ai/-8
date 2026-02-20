def calculate(expression):
    """
    Вычисляет значение арифметического выражения, содержащего круглые скобки,
    включая вложенные.

    Args:
        expression: Строка, представляющая арифметическое выражение.

    Returns:
        Значение выражения.
        Возвращает None, если выражение невалидно.
    """

    def precedence(operator):
        """Определяет приоритет операторов."""
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        return 0

    def apply_op(operators, values):
        """Применяет оператор к двум верхним значениям в стеке."""
        try:
            op = operators.pop()
            right = values.pop()
            left = values.pop()

            if op == '+':
                values.append(left + right)
            elif op == '-':
                values.append(left - right)
            elif op == '*':
                values.append(left * right)
            elif op == '/':
                if right == 0:
                    return None  # Обработка деления на ноль
                values.append(left / right)
        except IndexError:
            return None # Невалидное выражение, недостаточно операндов

        return True

    values = []
    operators = []
    i = 0

    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i] == '(':
            operators.append(expression[i])

        elif expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            i -= 1 # Корректировка индекса, т.к. цикл while увеличил i на 1 лишний раз

        elif expression[i] == ')':
            while len(operators) != 0 and operators[-1] != '(':
                if not apply_op(operators, values):
                    return None
            if len(operators) != 0 and operators[-1] == '(':
                operators.pop()
            else:
                return None # Несоответствие скобок

        elif expression[i] in ['+', '-', '*', '/']:
            while len(operators) != 0 and precedence(operators[-1]) >= precedence(expression[i]):
                if not apply_op(operators, values):
                    return None
            operators.append(expression[i])

        else:
            return None  # Невалидный символ

        i += 1

    while len(operators) != 0:
        if not apply_op(operators, values):
            return None

    if len(values) == 1:
        return values[0]
    else:
        return None  # Невалидное выражение, слишком много значений

# Примеры использования
print(calculate("10 + 2 * 6"))  # Output: 22
print(calculate("100 * ( 2 + 12 )"))  # Output: 1400
print(calculate("100 * ( 2 + 12 ) / 14"))  # Output: 100.0
print(calculate("( 1 + 2 ) * ( 3 + 4 )")) # Output: 21
print(calculate("10 / 0")) # Output: None
print(calculate("2 + (3 * 4)")) # Output: 14
print(calculate("2 + (3 * 4))")) # Output: None
print(calculate("(2 + 3 * 4")) # Output: None
print(calculate("2 + a")) # Output: None