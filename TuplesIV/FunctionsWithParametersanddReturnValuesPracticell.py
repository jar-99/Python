def compare(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3
    return greatest

def main():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))
    result = compare(num1, num2, num3)
    print("Greatest:", result)

if __name__ == "__main__":
    main()