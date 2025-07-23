
def encryption():
    #this is where the encoding wilo be stored
    encryption = {}
    try:
        file = open('codes.txt', 'r')
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                key, value = parts
                encryption[key] = value
                print(f"Adding code: {key} -> {value}")
        file.close()
        return encryption
    except FileNotFoundError:
        print("File not found. Please ensure 'codes.txt' exists.")
        return encryption
    
def main():
    codes = encryption()

    try:
        infile = open("original_message.txt", "r")
        outfile = open("encrypted.txt", "w")

        for line in infile:
            for char in line:
                if char in codes:
                    outfile.write(codes[char])
                else:
                    outfile.write(char)

        infile.close()
        outfile.close()
        print("Encryption complete.")

    except FileNotFoundError:
        print("original.txt not found.")

main()

# Decrypt a file using codes from codes.txt

# Decrypt a file using codes from codes.txt

def load_reverse_codes():
    decode = {}
    try:
        file = open("codes.txt", "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                original = parts[0]
                code = parts[1]
                decode[code] = original
        file.close()
    except FileNotFoundError:
        print("codes.txt not found.")
    return decode

def main():
    decode = load_reverse_codes()

    try:
        infile = open("encrypted.txt", "r")

        print("Decrypted message:")
        for line in infile:
            for char in line:
                if char in decode:
                    print(decode[char], end='')
                else:
                    print(char, end='')

        infile.close()

    except FileNotFoundError:
        print("encrypted.txt not found.")

main()