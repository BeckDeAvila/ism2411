
# 1. In Exercise 5, the first bug was spotted from the traceback and print statement. 
#    This shows my debugging instincts rely heavily on direct error messages and code tracing.
# 2. apply_discount(price, tier) takes a numeric price and a text membership tier, 
#    calculates the correct percentage reduction based on gold/silver/bronze/none, 
#    and returns the new discounted price. A colleague could use it easily.
# 3. Ai helped me, but it most defineltey shortcutted my knowledge


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

final_tax_amount = discounted_price + calculate_tax(discounted_price, 0.07)
print(f"After tax: ${final_tax_amount:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    total = discounted + calculate_tax(discounted, tax_rate)
    return total

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

# Fix 1: Add each sale instead of replacing the total
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Fix 2: Add the missing colon
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Fix 3: Stop the loop before going past the list
i = 0
while i < len(sales):
    print(sales[i])
    i += 1
    
# Fixed version of broken_sales.py goes here
# I found three problems. The total wasn't adding up, a colon was missing, and the loop went too far. AI helped explain the error, and I fixed the code. Now it works and shows $715 and 5 sales.I found three problems. The total wasn't adding up, a colon was missing, and the loop went too far. AI helped explain the error, and I fixed the code. Now it works and shows $715 and 5 sales.I found three problems. The total wasn't adding up, a colon was missing, and the loop went too far. AI helped explain the error, and I fixed the code. Now it works and shows $715 and 5 sales.I found three problems. The total wasn't adding up, a colon was missing, and the loop went too far. AI helped explain the error, and I fixed the code. Now it works and shows $715 and 5 sales.


# --- Exercise 6 ---

x = 100   # global variable

def double_it():
    x = 999   # local variable - different from global x!
    return x * 2

print(x)           # prints the global x (100)
print(double_it()) # prints the local calculation (1998)
print(x)           # prints the global x again, which did not change (100)
# The variable x inside the function is local, so it does not affect the global x outside.