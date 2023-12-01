def collatzConjecture():
    number = int(input("Enter a number: "))
    steps = 0

    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        steps += 1

    return steps

steps = collatzConjecture()
print("Steps taken:", steps)