n = int(input())
if n % 2 != 0:
    print("small")
elif n in range(21, 35):
    print("large")
elif n in range(2, 6):
    print("small")
else:
    print("large")
