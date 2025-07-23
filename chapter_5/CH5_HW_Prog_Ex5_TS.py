

# Request user input for replacement cost
replacement_cost = float(input("input replacement cost of building: $"))

# Calculate 80%
insurance_amount = replacement_cost * 0.80

# Show result
print(f"Min amount to insure property is: ${insurance_amount:,.2f}")