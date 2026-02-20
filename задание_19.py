import textwrap

def format_text_wrap_justify(text, column_width):
    wrapped_text = textwrap.fill(text, width=column_width, replace_whitespace=False, break_on_hyphens=False)
    words = wrapped_text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= column_width:
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                spaces = column_width - current_length
                if len(current_line) > 1:
                    base_spaces = spaces // (len(current_line) - 1)
                    extra_spaces = spaces % (len(current_line) - 1)
                    line = ' '.join(f"{word}{' ' * (base_spaces + (1 if i < extra_spaces else 0))}" for i, word in enumerate(current_line))
                else:
                    line = current_line[0].ljust(column_width)
                lines.append(line)
            current_line = [word]
            current_length = len(word)

    if current_line:
        lines.append(' '.join(current_line).ljust(column_width))

    return lines

# Don't work properly