first_integer = int(input("Enter the first integer: "))
second_integer = int(input("Enter the second integer: "))
third_integer = int(input("Enter the third integer: "))

print(f"{first_integer}{second_integer}{third_integer}")

if first_integer >= second_integer and first_integer >= third_integer:
    print("Yes")