def countdown():
    seconds = int(input("Enter the number of seconds: "))
    while seconds >= 0:
        print(seconds, end="... ")
        seconds -= 1

countdown()