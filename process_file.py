import json


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


def print_json_file(filename):
    with open(filename) as json_file:
        json_content = json.load(json_file)

    print(json.dumps(json_content, indent=4))


def get_from_json_file(filename, key):
    with open(filename) as json_file:
        json_content = json.load(json_file)

    return json_content[key]


def write_json_to_file(filename, json_obj):
    with open(filename, 'w') as json_file:
        json.dump(json_obj, json_file, indent=4)


if __name__ == "__main__":
    print_lines("hello_text.txt", [1, 4])
    insert_line_at("hello_text.txt", "Adding this line through Python.", 3)
    print_lines("hello_text.txt", [3])
    print_json_file("hello_json.json")
    my_string = get_from_json_file("hello_json.json", "string")
    print(my_string)
    my_dictionary = get_from_json_file("hello_json.json", "dictionary")
    write_json_to_file("dictionary.json", my_dictionary)
