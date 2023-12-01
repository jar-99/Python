def compare(a,b):
    if ord(a) > ord(b):
        return ord(a)
    else:
        return ord(b)

def main():
    a = input("Enter the first character: ")
    b = input("Enter the second character: ")
    result = compare(a, b)
    print("Result Value = ", result)

if __name__ == "__main__":
    main()