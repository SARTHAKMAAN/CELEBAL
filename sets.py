def calculate_average_unique_heights(height_list):
    unique_heights = set()
    
    for height in height_list:
        unique_heights.add(height)

    total_height = 0
    for height in unique_heights:
        total_height += height

    total_unique = 0
    for _ in unique_heights:
        total_unique += 1

    average_height = total_height / total_unique
    average_height = round(average_height, 3)

    return average_height

if __name__ == '__main__':
    num_heights = int(input("Enter number of heights: "))
    height_input = input("Enter the heights separated by space: ").split()
    heights = [int(height_input[i]) for i in range(num_heights)]

    result = calculate_average_unique_heights(heights)
    print("Average of distinct heights:", result)
