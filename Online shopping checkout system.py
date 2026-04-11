# 1. Personal Details
customer_name = "Santhiya"
age = 21
is_premium_member = True

# 2. Convert quantity from string to integer
quantity_str = "3"
quantity = int(quantity_str)

# 3. Price details
price_per_item = 499.99
total_amount = quantity * price_per_item

# 4. Apply discount
discount = total_amount * 0.10 if is_premium_member else 0
final_amount = total_amount - discount

# 5. Address swapping
delivery_address = "12, Gandhi Street, Chennai"
billing_address = "45, Nehru Nagar, Madurai"
delivery_address, billing_address = billing_address, delivery_address

# Output
print("Customer Name:", customer_name)
print("Age:", age)
print("Premium Member:", is_premium_member)
print("Quantity:", quantity)
print("Total Amount:", total_amount)
print("Discount:", discount)
print("Final Amount:", final_amount)
print("Delivery Address:", delivery_address)
print("Billing Address:", billing_address)
