

# Ask the user to enter the actual value of the property
actual_value = float(input("Enter the actual value of the property: $"))

# The assessment value is 60% of the actual value
assessment_value = actual_value * 0.60

# Property tax is $0.72 for every $100 of the assessment value
property_tax = (assessment_value / 100) * 0.72

# Display the results with two decimal places and comma formatting
print(f"Assessment value: ${assessment_value:,.2f}")
print(f"Property tax: ${property_tax:,.2f}")