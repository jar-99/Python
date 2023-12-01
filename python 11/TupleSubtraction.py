def tuple_subtraction(a, b):

    if len(a) != len(b):
        raise ValueError("The two tuples must have the same length.")

    result = tuple(i - j for i, j in zip(a, b))
    return result

a = tuple(int(x) for x in input("Enter the first tuple of integers: ").split())
b = tuple(int(x) for x in input("Enter the second tuple of integers: ").split())

result = tuple_subtraction(a, b)
print("Tuple Subtraction Result:", result)