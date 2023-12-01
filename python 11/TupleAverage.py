def tuple_average(t):
    return sum(t) / len(t)

print("Enter a tuple of numbers separated by space:", end=" ")
t = tuple(map(float, input().split()))
average = tuple_average(t)
print("The average of", t, "is", average)