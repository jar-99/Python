def check_order(num1, num2, num3):
    if num1 < num2 < num3:
        print("Ascending order.")
    elif num1 > num2 > num3:
        print("Descending order.")
    else:
        print("Random order.")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

check_order(first_number, second_number, third_number)
