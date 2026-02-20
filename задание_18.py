def format_text_into_columns(text, column_width):
    """
    Форматирует текст в колонки заданной ширины, перенося слова и равномерно
    распределяя пробелы между ними.

    Args:
        text: Текст для форматирования.
        column_width: Ширина одной колонки (количество символов).

    Returns:
        Строка, представляющая текст, отформатированный в колонки.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) == 0:
            current_line += word
        elif len(current_line) + len(word) + 1 <= column_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    # Равномерное распределение пробелов
    formatted_lines = []
    for line in lines:
        words_in_line = line.split()
        num_words = len(words_in_line)
        if num_words > 1:
            spaces_needed = column_width - sum(len(word) for word in words_in_line)
            spaces_between_words = spaces_needed // (num_words - 1)
            extra_spaces = spaces_needed % (num_words - 1)

            formatted_line = ""
            for i, word in enumerate(words_in_line):
                formatted_line += word
                if i < num_words - 1:
                    formatted_line += " " * spaces_between_words
                    if i < extra_spaces:
                        formatted_line += " "
        else:
            formatted_line = line

        formatted_lines.append(formatted_line)


    return "\n".join(formatted_lines)

# Пример использования:
text = "Это длинный текст, который нужно отформатировать в колонки заданной ширины.  Мы хотим, чтобы слова переносились в следующую строку, и чтобы пробелы между словами были распределены равномерно."
column_width = 30

formatted_text = format_text_into_columns(text, column_width)
print(formatted_text)