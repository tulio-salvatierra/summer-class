import random
import time


random_number = random.randint(0, 20)

while True:
    try:
        attempts = int(input("Choose the number of attemps, 5 or 10: "))
        if attempts not in [5, 10]:
            print("Invalid, enter 5 or 10. ")
        else:
            break
    except ValueError:
        print("Invalid, enter 5 or 10. ")

print("\nWelcome to guess the number!")
print(f"You have {attempts} attemps to guess a magic number betweeen 0 and 20.")

for attempt in range (1, attempts + 1):
    try:
        print(f"Attempt {attempt} of {attempts}")
        start_time = time.time()
        guess = int(input("Enter your guess: "))

        if time.time() - start_time > 5:
            print("Times up! You took too long to guess.")
            continue
        if guess == random_number:
            print(f"Congratulations! You guessed the magic number in {attempt} attempts.")
            break
        elif guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 20.")

if guess != random_number:
    print(f"Sorry, you did not guess the magic number. It was {random_number}.")    
print("Game over!")


