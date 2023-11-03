def count_integers():
    positive_count = 0
    negative_count = 0
    zero_count = 0

    try:
        for i in range(5):
            num = int(input(f"Enter {i + 1} integer: "))
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
            else:
                zero_count += 1

        print(f"Positive count: {positive_count}")
        print(f"Negative count: {negative_count}")
        print(f"Zero count: {zero_count}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

count_integers()