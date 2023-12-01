def printHelloMessage(n):
    if n > 0:
        for i in range(n):
            print("Hello!, from CodeChum")
    else:
        print("Error: n must be a positive integer.")


n = int(input("Enter a positive integer: "))


printHelloMessage(n)