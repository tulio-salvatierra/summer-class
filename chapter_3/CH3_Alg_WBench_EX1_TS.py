# Excersice 1: Display a message five times
for _ in range(5):
    print("I love Python programming!")

# Excersice 2: Display numbers from 1 to 100
for number in range(1, 101):
    print(number)

# Excersice 3: Display odd numbers from 1 to 49
for number in range(1, 50, 2):
    print(number)

# Excersice 4: Prompt for number of times to print a message
times = int(input("How many times should I say hello? "))
for _ in range(times):
    print("Hello")

# Excersice 5: Get a number and display the square of numbers up to that number
max_num = int(input("Enter a positive integer: "))
for i in range(1, max_num + 1):
    print(f"{i} squared is {i**2}")

# Excersice 6: Calculate total and average of 5 test scores
total = 0
for i in range(5):
    score = float(input(f"Enter test score #{i+1}: "))
    total += score

# Excersice 6: Calculate total and average of 5 test scores
average = total / 5
print("Total:", total)
print("Average:", average)

# Excersice 7: Display a multiplication table for a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Excersice 8: Calculate compound interest for 10 years
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))

for year in range(1, 11):
    principal += principal * rate
    print(f"Year {year}: ${principal:.2f}")

# Excersice 9: Display a pattern of '#' in a 10x15 grid
for _ in range(10):
    print("#" * 15)

# Excersice 10: Validate that user enters a positive number
number = float(input("Enter a positive, nonzero number: "))
while number <= 0:
    print("Invalid input. Try again.")
    number = float(input("Enter a positive, nonzero number: "))

print("You entered:", number)