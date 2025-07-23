import random
def main():
    #empty list to hold the lottery numbers
    lottery_numbers = []

    #generate 7 unique random numbers between 0 and 9
    for i in range(7):
        digit = random.randint(0, 9)
        lottery_numbers.append(digit)

    #display the lottery numbers
    print("The lottery numbers are:")
    for number in lottery_numbers:
        print(number, end=' ')
    print()  # for a new line after the numbers

main()