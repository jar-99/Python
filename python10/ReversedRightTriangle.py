def print_number_pattern(size):
    for i in range(size + 1):
        print(str(i) * i)

size = int(input("Enter a number: "))

print_number_pattern(size)