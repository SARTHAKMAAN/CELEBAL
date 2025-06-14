def merge_tools(input_string, group_size):
    string_length = len(input_string)
    
    for start_index in range(0, string_length, group_size):
        substring = input_string[start_index:start_index + group_size]
        unique_characters = ""

        for character in substring:
            if character not in unique_characters:
                unique_characters += character

        print(unique_characters)


if __name__ == '__main__':
    input_string = input("Enter the string: ")
    group_size = int(input("Enter the group size: "))
    merge_tools(input_string, group_size)
