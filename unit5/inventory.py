# 1.
# I was surprised by how easy it is to mix different data types in the same list and use negative numbers to count backward from the end.

# 2. 
# would have saved you time compared to doing it manually in Excel.
# Pulling daily sales numbers and filtering out bad data or finding averages in Excel takes a bunch of manual clicks and formulas, whereas a quick Python list would calculate it instantly.

# EXERCISE 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# EXERCISE 2
# First item (positive 0, negative -len)
print(inventory[0])
# Last item (positive -1, negative -1)
print(inventory[-1])
# Middle item (computed using len)
mid_index = len(inventory) // 2
print(inventory[mid_index])

# EXERCISE 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# EXERCISE 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# EXERCISE 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable, which is useful for coordinates because it ensures fixed geographical data cannot be accidentally modified.")
print(coords)

# EXERCISE 6
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")

# EXERCISE 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.9, 2))

print("Original:", prices)
print("Discounted:", discounted)

# EXERCISE 8
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = [s for s in sales_data if s > 300]
high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print(f"{high_sales} | Count: {high_count} | Avg: {high_avg:.2f}")