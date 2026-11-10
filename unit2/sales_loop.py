
# SELF ASSESSMENT ANSWERS

# Initialize: Start with total = 0. This matters because it gives your loop a clean starting point.
# Loop: Look at each item one by one. This matters because it lets you process every piece of data.
# Update: Add each item to total. This matters because it builds up the final result step by step.

#. 2. For vs. While:
# While loops need extra code to handle counter variables.
# For loops do this automatically, making them shorter and safer from infinite loops.

# 3. Real Example (Air Pollution):
# List contains daily pollution numbers (PM2.5).
# Loop adds up daily numbers and counts high-pollution days.
# Print the average level and total bad days.


# Self Assesment Questions

# 1. The accumulator pattern is a technique used to aggregate or build up a result over time as you iterate through a collection of data. Its three key steps are:
#  - Initialize: Setting up a variable (e.g., total = 0) before starting the loop to hold the running total/state. This provides a baseline starting point.
#  - Loop: Iterating over each item in a collection sequentially.
# Update: Modifying the accumulator variable inside the loop with each iteration's data (e.g., total += sale). This steps through the data and updates the running aggregate.

# 2. The while loop requires manually tracking and incrementing an index variable (i = 0, i += 1), making the code longer and slightly more prone to infinite loop bugs if the counter update is missed. The for loop is cleaner and handles sequence iteration automatically. In production, a for loop is preferred for iterating over sequences because it is idiomatic, cleaner, and safer.

# 3. In an environmental science dataset measuring daily particulate matter (PM2.5) air quality readings, a list would contain numerical pollution concentrations for a month. A loop would accumulate the daily values into a running sum and track a count of days exceeding safety thresholds. At the end, it would print the monthly average PM2.5 level and the total number of days with poor air quality.

# --- Exercise 1 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# --- Exercise 2 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0
for sale in sales:
    total += sale
    count += 1
average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# --- Exercise 3 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
current_max = sales[0]
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest sale: ${current_max}")

# --- Exercise 4 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
count_over_100 = 0
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

# --- Exercise 5 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale <= 100:
        continue
    if sale > 400:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break
    print(f"${sale}")

# --- Exercise 6 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total: ${total}")

# --- Exercise 7 ---
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale >= 200:
        discount_pct = 10
    elif sale >= 100:
        discount_pct = 5
    else:
        discount_pct = 0
    
    discounted_price = sale * (1 - discount_pct / 100)
    print(f"${sale}  → {discount_pct}% discount → ${discounted_price:.2f}")