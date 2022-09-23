# CTF CODE INCOMIG .-.

import os
from termcolor import colored

root_path = os.path.dirname(os.path.abspath(__file__))

FIRST_HEX_DUMP_PATH: str = os.path.join(
    root_path, 'first_hex_goatman.hexdump'
)
SECOND_HEX_DUMP_PATH: str = os.path.join(
    root_path, 'second_hex_goatman.hexdump'
)

first_hex_dump: str = open(FIRST_HEX_DUMP_PATH, 'r').read()
second_hex_dump: str = open(SECOND_HEX_DUMP_PATH, 'r').read()


first_hex_dump_length: int = len(first_hex_dump)
second_hex_dump_length: int = len(second_hex_dump)

# def compare_values
first_line_buffer: str = ''
second_line_buffer: str = ''


comparison: dict[str, dict[str, str]] = dict()
count = 0

for i in range(max([first_hex_dump_length, second_hex_dump_length])):

    if first_hex_dump_length - 1 > i:
        first_element: str = first_hex_dump[i]

        if first_element == '\n':
            hex_prefix: str = first_line_buffer.split()[0]

            if first_line_buffer[:4] == '    ':
                hex_prefix += '_server'
            else:
                hex_prefix += '_client'
            raw_data: str = ' '.join(
                element for element in first_line_buffer.split()
                if len(element) == 2 and element[0] in '1234567890abcdef' and element[1] in '1234567890abcdef'
            )
            if hex_prefix not in comparison:
                comparison[hex_prefix] = dict()
            comparison[hex_prefix]['first'] = raw_data

            first_line_buffer = ''

        else:
            first_line_buffer += first_element

    if second_hex_dump_length - 1 > i:
        second_element: str = second_hex_dump[i]

        if second_element == '\n':
            hex_prefix: str = second_line_buffer.split()[0]

            if second_line_buffer[:4] == '    ':
                hex_prefix += '_server'
            else:
                hex_prefix += '_client'
            raw_data: str = ' '.join(
                element for element in second_line_buffer.split()
                if len(element) == 2 and element[0] in '1234567890abcdf' and element[1] in '1234567890abcdf'
            )
            if hex_prefix not in comparison:
                comparison[hex_prefix] = dict()
            comparison[hex_prefix]['second'] = raw_data

            second_line_buffer = ''

        else:
            second_line_buffer += second_element


parsed_values: dict[str, str] = dict()

max_value: int = 0

for key, dumps_ in comparison.items():
    if len(dumps_) == 2:

        first: list[str] = dumps_['first'].split()
        second: list[str] = dumps_['second'].split()

        first_buffer: list[str] = list()
        second_buffer: list[str] = list()

        for i in range(min([len(first), len(second)])):

            if len(first) - 1 > i:
                first_element: str = first[i]

            if len(second) - 1 > i:
                second_element: str = second[i]

            first_buffer.append(
                colored(first_element, 'red')
                if first_element == second_element
                else first_element
            )
            second_buffer.append(
                colored(second_element, 'red')
                if first_element == second_element
                else second_element
            )
        if max_value < len(first_buffer)*3 - 1:
            max_value = len(first_buffer)*3 - 1

        parsed_values[key] = f'\'{" ".join(first_buffer)}\'  |  \'second\': \'{" ".join(second_buffer)}\''


print(max_value)
# print(
#     ('60 f5 29 e7 0f bf 14 ac a8 9d 2d 71 7d e3 07 07'.split())
#     )
for key, parsed_ in parsed_values.items():

    print(key, parsed_)
    # first_parsed, second_parsed = parsed_.split(" | ")

    # print(len(
    #     parsed_.split(' | ')[0]), parsed_.split(' | ')[0])

    # if len(first_parsed) <= max_value:
    #     first_parsed += ' '*(max_value - len(first_parsed))

    # first_parsed += ' |'

    # print(key, first_parsed, second_parsed, len(
    #     parsed_.split(' | ')[0]), parsed_.split(' | ')[0])
