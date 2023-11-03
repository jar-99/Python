def categorize_person(age, height):
    if age >= 18 and height > 0:
        if 18 <= age <= 30:
            if height > 170:
                print("Young and Tall")
            else:
                print("Young and Short")
        elif 31 <= age <= 50:
            if height > 170:
                print("Middle-aged and Tall")
            else:
                print("Middle-aged and Short")
        else:
            if height > 170:
                print("Old and Tall")
            else:
                print("Old and Short")
    else:
        print("Invalid input: Age should be 18 or older, and height should be a positive value.")

age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

categorize_person(age, height)