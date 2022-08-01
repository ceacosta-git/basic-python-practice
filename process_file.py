def print_lines(filename, line_numbers):
    lines = []
    with open(filename) as text_file:
        lines = text_file.readlines()

    for line_number in line_numbers:
        print(lines[line_number - 1], end="")

    print("")


def insert_line_at(filename, line, line_number):
    with open(filename) as text_file:
        lines = text_file.readlines()

    lines.insert(line_number - 1, f'{line}\n')

    with open(filename, 'w') as text_file:
        new_content = "".join(lines)
        text_file.writelines(new_content)


if __name__ == "__main__":
    print_lines("hello_text.txt", [1, 4])
    insert_line_at("hello_text.txt", "Adding this line through Python.", 3)
    print_lines("hello_text.txt", [3])