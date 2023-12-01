def lionelRichie():
    for i in range(1000):
        print("Hi I am okay, do you copy?")

def main():
    x = int(input("Enter a number: "))
    for i in range(1, x+1):
        if i % 2 == 0 or i % 3 == 0:
            lionelRichie()
        else:
            print(i)

main()