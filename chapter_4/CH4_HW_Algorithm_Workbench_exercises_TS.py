

# Tulio Salvatierra

# Exercise 1: 

product = 0

while product < 100:
    number = int(input("Enter a number: "))
    product = number * 10
    print("product is: ", product)

# Exercise 2:

repeat = "y"

while repeat.lower() == "y":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print("The total is: ", total)

    repeat = input("Do you want to repeat? (y/n): ")

# Exercise 3:

for i in range(0, 1001, 10):
    print(i, end=", ")

# Exercise 4:

total = 0

for i in range(10):
    num = float(input(f"Enter number #{i+1}: "))
    total += num

print("The total sum is:", total)

# Exercise 5:

total = 0

for numerator in range(1, 31):
    denominator = 31 - numerator
    total += numerator / denominator

print("The total sum is: ", total)

# Exercise 6:

# a.
x = 0  # Initialize x
x += 1

# b.
x *= 2

# c.
x /= 10

# d.
x -= 100

#Excercise 7:

for row in range(10):
    for col in range(15):
        print("#", end="")
    print()

# Exercise 8:

while True:
    try:
        number = float(input("Enter a positive, nonzero number: "))
        if number > 0:
            print("Valid input! You entered:", number)
            break
        else:
            print("Error: The number must be greater than zero.")
    except ValueError:
        print("Error: Please enter a valid number.")

# Exercise 9:

while True:
    try:
        number = int(input("Enter a number between 1 and 100: "))
        if 1 <= number <= 100:
            print("Valid input! You entered:", number)
            break
        else:
            print("Error: Number must be between 1 and 100.")
    except ValueError:
        print("Error: Please enter a valid integer.")