num_elements = int(input("Enter the number of elements: "))

number_set = set(map(int, input("Enter the elements separated by space: ").split()))

num_operations = int(input("Enter the number of operations: "))


for _ in range(num_operations):
    operation = input("Enter operation: ").strip().split()

    if operation[0] == "pop":
        if len(number_set) > 0:
            number_set.pop()
    elif operation[0] == "remove":
        value_to_remove = int(operation[1])
        if value_to_remove in number_set:
            number_set.remove(value_to_remove)
    elif operation[0] == "discard":
        value_to_discard = int(operation[1])
        number_set.discard(value_to_discard)

print("Sum of remaining elements:", sum(number_set))
