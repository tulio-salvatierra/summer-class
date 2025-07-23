
import random

def main():
    # Ask user for how many numbers to write
    count = int(input("How many random numbers should I write to the file? "))

    with open("./random_numbers.txt", "w") as file:
        for _ in range(count):
            number = random.randint(1, 500)
            file.write(f"{number}\n")

    print(f"{count} random numbers written to random_numbers.txt.")

if __name__ == "__main__":
    main()