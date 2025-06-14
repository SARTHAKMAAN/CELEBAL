def print_alphabet_rangoli(size):
    import string
    letters = string.ascii_lowercase  # List of lowercase alphabets
    pattern_lines = []

    for row_index in range(size):
        left_part = letters[size-1:row_index:-1]   # Left half excluding center
        right_part = letters[row_index:size]       # Center to right
        row_pattern = '-'.join(left_part + right_part)  # Join with dashes
        centered_row = row_pattern.center(4 * size - 3, '-')  # Center-align
        pattern_lines.append(centered_row)

    # Print the full rangoli: top (reversed), center, bottom
    for line in pattern_lines[::-1] + pattern_lines[1:]:
        print(line)

if __name__ == '__main__':
    n = int(input("Enter the Size: "))
    print_alphabet_rangoli(n)
