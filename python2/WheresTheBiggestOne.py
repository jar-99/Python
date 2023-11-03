def locate_largest_position(a, b, c, d, e):
    numbers = [a, b, c, d, e]
    max_num = max(numbers)

    if max_num == a:
        print("Leftmost")
    elif max_num == c:
        print("Middle")
    elif max_num == e:
        print("Rightmost")
    else:
        print("Unknown")

first_int = int(input("First integer: "))
second_int = int(input("Second integer: "))
third_int = int(input("Third integer: "))
fourth_int = int(input("Fourth integer: "))
fifth_int = int(input("Fifth integer: "))

locate_largest_position(first_int, second_int, third_int, fourth_int, fifth_int)
