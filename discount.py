# user for the total purchase amount
purchase_amount = float(input("Enter the total purchase amount: "))

# Determine the discount rate
if purchase_amount > 5000:
    discount_rate = 0.25
elif purchase_amount >= 3000:
    discount_rate = 0.15
elif purchase_amount >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

# Calculate discount and final amount
discount = purchase_amount * discount_rate
final_price = purchase_amount - discount
