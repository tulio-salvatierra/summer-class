

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
hoursWorked = int(input("Please enter the number of hours worked: "))

hourlyRate = 15.00

Weekly = hoursWorked * hourlyRate

biWeekly = Weekly * 2   

monthly = Weekly * 4

yearly = monthly * 12

print("\n")
print(f"{firstName} {lastName}")
print(f"-----------------------------------") 
print(f"Hours worked: {hoursWorked}")
print(f"Hourly rate: {hourlyRate}")
print(f"-----------------------------------")

print(f"Your biweekly pay is: {biWeekly}")
print(f"Your monthly pay is: {monthly}")
print(f"Your yearly pay is: {yearly}")
