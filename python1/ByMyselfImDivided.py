number = int(input("Enter a three-digit number: "))

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

digit_sum = digit1 + digit2 + digit3

if number % digit_sum == 0:
    print("It's divisible by the sum of its digits.")
else:
    print("It's not divisible by the sum of its digits.")