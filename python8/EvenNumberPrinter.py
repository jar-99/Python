def printEvenNumbers(n):
    n = int(input("Enter a positive integer : "))

    while n >= 1:
        if n % 2 == 0:
            print(n)
        n -= 1

printEvenNumbers(10)