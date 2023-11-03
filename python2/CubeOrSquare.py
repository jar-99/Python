def cube_or_square(num):
    if num < 0:
        print(f"Cube = {num ** 3}")
    elif num > 0:
        print(f"Square = {num ** 2}")
    else:
        print("Zero")

number_shown = float(input("Enter the number: "))
cube_or_square(number_shown)