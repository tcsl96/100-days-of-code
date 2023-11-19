from random import randint

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = [None]*(nr_letters + nr_symbols + nr_numbers)

for _ in range(nr_letters):
    while (True):
        i = randint(0, len(password) - 1)
        if (password[i] == None):
            while (True):
                j = randint(0, len(letters) - 1)
                if (letters[j] not in password):
                    password[i] = letters[j]
                    break
            break
for _ in range(nr_symbols):
    while (True):
        i = randint(0, len(password) - 1)
        if (password[i] == None):
            while (True):
                j = randint(0, len(symbols) - 1)
                if (symbols[j] not in password):
                    password[i] = symbols[j]
                    break
            break
for _ in range(nr_numbers):
    while (True):
        i = randint(0, len(password) - 1)
        if (password[i] == None):
            while (True):
                j = randint(0, len(numbers) - 1)
                if (numbers[j] not in password):
                    password[i] = numbers[j]
                    break
            break

print("".join(password))