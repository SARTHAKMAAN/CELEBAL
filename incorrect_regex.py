import re

total_patterns = int(input("Enter number of patterns to check: "))
for _ in range(total_patterns):
    regex_pattern = input("Enter regex pattern: ")
    try:
        re.compile(regex_pattern)
        print(True)
    except re.error:
        print(False)
