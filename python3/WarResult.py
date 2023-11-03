def war_results(first_num, second_num, percentage_value):
    if first_num > second_num:
        calculated_percentage = (first_num * percentage_value) / 100
        if calculated_percentage > second_num:
            print("I am greater even when I am divided.")
        elif calculated_percentage > (second_num / 2):
            print("When you are divided, you fall.")
        else:
            print("I cannot afford to lose some people.")
    else:
        print("This is unwinnable.")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
percentage = float(input("Enter the percentage value: "))

war_results(first_number, second_number, percentage)