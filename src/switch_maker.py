"""
    This file is just a simple script that was used to generate the GIGANTIC case statement
    used in the main file to decode key press event numbers into their associated key values
    strings. It takes an edited version of the type definitions found in 
    /usr/include/linux/input-event-codes.h and from them generates the switch statement
    although some assembly is required...
    Included for completeness and in case the definitions ever change.
"""

def text_to_lines(input_text):
    raw_lines = input_text.split('\n')
    out_lines = []
    for raw_line in raw_lines:
        if raw_line.strip() != '':
            raw_line = raw_line.strip().split(' ')[1].split('\t')
            out_lines.append((raw_line[-1],raw_line[0]))
    return out_lines

def generate_switch(input_text:str) -> None:
    lines = text_to_lines(input_text)
    for line in lines:
        print(f"case {line[0]}:")
        print(f'\treturn "{line[1]}";')

def main():
    fd = open('input.txt','r')
    input_text = fd.read()
    generate_switch(input_text)

if __name__ == "__main__":
    main()
