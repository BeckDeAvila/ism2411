# --- QUESTIONS ---
#
# 1. Python won't crash it will run completely fine.
#    However, using 10 instead of 0.10 means the math would calculate a 1000% discount instead of a 10% discount. 
#    This creates a logic error where the math gives completely wrong numbers.
#
# 2. Setting up employee shift scheduling or work teams. 
#    For example, if you have 25 workers and need groups of 4 per project, floor division tells you how many full 4-person teams you can make , and modulo tells you how many extra employees are left without a full team.
#
# 3. Remembering all the different f-string formatting rules.
#    A few more real world examples with different number formats would help.

# --- Exercise 1 ---
price = 50
quantity = 12
revenue = price * quantity

print(f"Revenue: ${revenue:,.2f}")

# --- Exercise 2 ---
cost = 32
price = 50
margin = (price - cost) / price

print(f"Margin: {margin:.1%}")

# --- Exercise 3 ---
cost_a, price_a = 25, 45
cost_b, price_b = 30, 50

margin_a = (price_a - cost_a) / price_a
margin_b = (price_b - cost_b) / price_b

product_a_wins = margin_a > margin_b

print(f"Product A Margin: {margin_a:.1%}")
print(f"Product B Margin: {margin_b:.1%}")
print(f"Product A has a higher margin: {product_a_wins}")

# --- Exercise 4 ---
price = 150
margin = 0.35

is_premium = (price > 100) and (margin > 0.3)
print(f"is_premium (price=${price}, margin={margin:.1%}): {is_premium}")

price = 120
margin = 0.20

is_premium = (price > 100) and (margin > 0.3)
print(f"is_premium (price=${price}, margin={margin:.1%}): {is_premium}")

# --- Exercise 5 ---

res_div = 17 / 5
print(f"17 / 5 = {res_div}")

res_floor = 17 // 5
print(f"17 // 5 = {res_floor}")

res_mod = 17 % 5
print(f"17 % 5 = {res_mod}")

# --- Exercise 6 ---

product_name = input("Enter product name: ")
retail_price = float(input("Enter retail price: "))
unit_cost = float(input("Enter unit cost: "))
quantity_sold = int(input("Enter quantity sold: "))
discount_pct = float(input("Enter discount percentage (e.g., 10 for 10%): "))

revenue = retail_price * quantity_sold
discounted_price = retail_price * (1 - discount_pct / 100)
discounted_revenue = discounted_price * quantity_sold
gross_margin = (retail_price - unit_cost) / retail_price
net_profit = discounted_revenue - (unit_cost * quantity_sold)

print(f"Product Name: {product_name}")
print(f"Revenue (before discount): ${revenue:,.2f}")
print(f"Discounted Revenue: ${discounted_revenue:,.2f}")
print(f"Gross Margin: {gross_margin:.1%}")
print(f"Net Profit: ${net_profit:,.2f}")

# --- Exercise 7 ---

items_ordered = int(input("Enter the number of items ordered: "))

BOX_CAPACITY = 24

full_boxes = items_ordered // BOX_CAPACITY
loose_items = items_ordered % BOX_CAPACITY
exact_fit = loose_items == 0

print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")