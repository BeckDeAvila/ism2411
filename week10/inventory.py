
# Questions
# I was surprised that Python lists can be changed after they are created.
# I also learned that negative indices make it easy to access the last items.
#
# When I coached swimming, I could have used a Python list to track swimmers' times.
# It would have helped me calculate averages and find the fastest times without manually checking Excel.

# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which keeps coordinates consistent.")
print(coords)

# Exercise 6
sales = [100, 250, 75, 480, 200]
print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
