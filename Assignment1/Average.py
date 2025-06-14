if __name__ == '__main__':
    n = int(input("How many students? "))
    student_marks = {}

    for _ in range(n):
        data = input("Enter name and marks:").split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks

    query_name = input("Whose average do you want? ")
    average = sum(student_marks[query_name]) / 3

    print("Average marks:")
    print(f"{average:.2f}")
