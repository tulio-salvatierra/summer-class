def main():
    numbers = get_values()

    print("The numbers you entered are:", numbers)
def get_values():
    values = []
    again = "y"

    while again == "y":
        num = int(input("Enter a number: "))
        values.append(num)

        print("Do you want to enter another number? (y/n)")
        again = input('y = yes, n = no: ')
        print()

    return values
if __name__ == "__main__":
    main()
    


