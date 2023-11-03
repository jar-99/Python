def alcohol_purchase_validator(age):
    if age >= 21:
        valid_id = input("Do you have a valid ID? (y/n): ")
        if valid_id == 'y':
            print("Can purchase alcohol")
        else:
            print("Cannot purchase alcohol without a valid ID")
    else:
        print("Ineligible to purchase alcohol")

age = int(input("Enter your age: "))
alcohol_purchase_validator(age)