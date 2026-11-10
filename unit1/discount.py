# Self Assessment Answers

# 1. First the total of 350 gets checked if it is 500 or more.
# It is not so it moves to the next check.
# Next it checks if 350 is 200 or more.
# It is so it stops there and gets a 10% discount.

# 2. Using 'and' in one statement makes both things must be true at the same time.
# Two separate 'if' statements check each thing on its own.
# They are not always the same because separate 'if' checks can be different.

# 3. We see tiered rules in things like tax rates and shipping costs.
# Knowing Python shows that these rules are just simple 'if' and 'else' steps.
# It makes it easy to see how systems choose prices or points based on numbers.

# --- Exercise 1 ---
total = float(input("Enter cart total: $"))
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0.0
final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 2 ---
if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")

# --- Exercise 3 ---
region = "South"
total = 250
if total >= 500:
    tier_discount = 0.15
elif total >= 200:
    tier_discount = 0.10
elif total >= 100:
    tier_discount = 0.05
else:
    tier_discount = 0.0

if region == "South":
    print("Region bonus applied: additional 2% off")
    extra = 0.02
else:
    extra = 0.0

final_discount = tier_discount + extra
final = total * (1 - final_discount)
print(f"Final discount: {final_discount*100:.0f}%")
print(f"Final price: ${final:.2f}")

# --- Exercise 4 ---
# The flat version using 'and' is easier to read and test because it avoids deep indentation and reduces cognitive complexity, allowing all conditions to be evaluated in a single clear statement.
if region == "South" and total > 100 and customer_type == "wholesale":
    extra_discount = 0.03

# --- Exercise 5 ---
amount = 15000
if 1 <= amount <= 9999:
    print("NORMAL")
elif amount <= 0:
    print("SUSPICIOUS")
elif amount >= 10000:
    print("LARGE — REVIEW REQUIRED")

# --- Exercise 6 ---
annual_spend = 2500
orders_placed = 8
outstanding_balance = False

qualifies = (annual_spend > 2000 or orders_placed > 10) and not outstanding_balance
if qualifies:
    print("VIP upgrade approved")