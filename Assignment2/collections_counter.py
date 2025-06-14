from collections import Counter

total_shoes = int(input("Enter number of shoes in the shop: "))
available_sizes = list(map(int, input("Enter shoe sizes: ").split()))
shoe_inventory = Counter(available_sizes)

total_customers = int(input("Enter number of customers: "))
total_earnings = 0

for _ in range(total_customers):
    requested_size, offered_price = map(int, input("Enter size and price: ").split())

    if shoe_inventory[requested_size] > 0:
        total_earnings += offered_price
        shoe_inventory[requested_size] -= 1

print("Total earnings:", total_earnings)
