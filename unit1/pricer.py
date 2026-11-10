# --- Exercise 5 ---
type("12")  -> <class 'str'>   (Text inside quotes is a String)
type(12)    -> <class 'int'>   (Whole numbers without decimals are Integers)
type(12.0)  -> <class 'float'> (Numbers with decimals are Floats)
type(True)  -> <class 'bool'>  (Boolean truth values)

# Self Assessment Questions 
# 1. Error: TypeError: can't multiply sequence by non-int of type 'float'.
# This happens because input() gives text, and Python cannot multiply text by a float.

# 2. "5" + "3" joins text to get "53", while 5 + 3 adds numbers to get 8.
# Since input() returns text, you have to use float() or int() before doing math.

# 3. In business, I can put revenue and cost into variables and use f-strings to print clean summary reports automatically.



# --- Exercise 1 ---
product = "paper"
unit_price = 0.99
quantity = 100
in_stock = True

print(type(product))
print(type(unit_price))
print(type(quantity))
print(type(in_stock))

# --- Exercise 2 ---
print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity:.2f}")

# --- Exercise 3 ---
product = input("Enter product name: ")
unit_price = float(input("Enter unit price: "))
quantity = int(input("Enter quantity: "))

print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity:.2f}")

# --- Exercise 4 ---
unit_cost = 0.50  # Set a unit cost below price to show a standard margin calculation
revenue = unit_price * quantity
margin = (revenue - (unit_cost * quantity)) / revenue if revenue > 0 else 0.0

print(f"Product:  {product}")
print(f"Price:    ${unit_price:.2f}")
print(f"Qty:      {quantity}")
print(f"Revenue:  ${revenue:.2f}")
print(f"Margin:   {margin:.1%}")