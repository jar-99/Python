def remove_elements(tuple1, tuple2):
    result = ()

    for i in tuple1:
        if i not in tuple2:
            result += (i,)

    return result

x = int(input("Enter the size of tuple1: "))
tuple1 = tuple(str(input(f"Enter element {i+1} of tuple1: ")) for i in range(x))

y = int(input("Enter the size of tuple2: "))
tuple2 = tuple(str(input(f"Enter element {i+1} of tuple2: ")) for i in range(y))

result = remove_elements(tuple1, tuple2)
combined = tuple1 + tuple2
combined_result = combined + result
print(combined_result)