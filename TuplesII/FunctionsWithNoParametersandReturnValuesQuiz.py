def banner():
    print("CodyChum")

def main():
    x = int(input("Enter a number: "))
    for i in range(1, x+1):
        if i % 2 == 0 or i % 3 == 0:
            banner()
        else:
            print(i)

main()