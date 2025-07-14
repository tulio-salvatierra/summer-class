## 1. Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.

def times_ten(number):
    print(number * 10)

# 2. Examine the following function header, then write a statement that calls the function, passing 12 as an argument.
# def show_value(quantity):   

def show_value(quantity):
    show_value(12)
    
# 3. Look at the following function header:
# def my_function(a, b, c):
# Now look at the following call to my_function:
# my_function (3, 2, 1)
# When this call executes, what value will be assigned to a? What value will be assigned to b? What value will be assigned to C?

def my_function(a, b, c):
    my_function(3, 2, 1)


# 4. What will the following program display?

def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)
def change_us(a, b):
    a = 0
    b= 0
    print(a, b)
main()

# The program will display:
# 1 3.4
# 1 3.4
# 0 0
# The values of x and y in the main function remain unchanged after the call to change_us.

# 5. Look at the following function definition:
def my_function(a, b, c):
    d = (a+ c) / b
    print(d)

# a. Write a statement that calls this function and uses keyword arguments to pass 2 into a, 4 into b, and 6 into C.
#100 and assigns it to a variable named rand.

my_function(a=2, b=4, c=6)

# b. What value will be displayed when the function is called?

2.0

# 6. Write a statement that generates a random number in the range of 1 through
# 100 and assigns it to a variable named rand.

import random

rand = random.randint(1, 100)

# 7. The following statement calls a function named half, which returns a value that is half that of the argument. (Assume the number variable references a float value.)
# Write code for the function.

def half(value):
    return value / 2

number = 10  # Define a value for number
result = half(number)

# 8. A program contains the following function definition:
 
def cube(num):
    return num * num * num

result = cube(4)  

# 9. Write a function named times_ten that accepts a number as an argument.
# When the function is called, it should return the value of its argument multiplied times 10.

def times_ten(number):
    return number * 10
# Example usage:
result = times_ten(5)  # result will be 50

# 10. Write a function named get_first_name that asks the user to enter his or her first name, and returns it.

def get_first_name():
    first_name = input("Enter your first name: ")
    return first_name

