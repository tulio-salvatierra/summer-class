
def main():
    total = 0
    count = 0

    try:
        with open("random_numbers.txt", "r") as file:
            for line in file:
                number = int(line.strip())
                print(number)
                total += number
                count += 1

        print("\nSummary:")
        print(f"Total of numbers: {total}")
        print(f"Number of values read: {count}")

    except FileNotFoundError:
        print("Error: random_numbers.txt not found. Run EX7 first.")

if __name__ == "__main__":
    main()