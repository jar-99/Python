import math

def get_double():
    while True:
        try:
            number = float(input("Enter a number: "))
            if number <= 0:
                return number
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

total = 0.0

while True:
    user_input = get_double()

    if user_input <= 0:
        break

    total += user_input

print("Sum: {:.2f}".format(total))