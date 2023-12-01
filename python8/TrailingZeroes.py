def countTrailingZeroes(number):
    count = 0
    while number % 10 == 0:
        number = number / 10
        count += 1
    return count

number = int(input("Enter a number : "))
print("Number of trailing zeroes : ", countTrailingZeroes(number))