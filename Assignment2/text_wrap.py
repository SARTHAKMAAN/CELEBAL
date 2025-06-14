import textwrap

def wrap_text_by_width(input_text, line_width):
    wrapped_lines = textwrap.wrap(input_text, width=line_width)
    formatted_output = '\n'.join(wrapped_lines)
    return formatted_output

if __name__ == '__main__':
    input_text = input("Enter the string: ")
    line_width = int(input("Enter the width: "))
    result = wrap_text_by_width(input_text, line_width)
    print(result)
