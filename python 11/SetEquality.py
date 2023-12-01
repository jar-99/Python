def set_equality(set1, set2):
    return set1 == set2

set1 = input("Enter the first set: ").split()
set2 = input("Enter the second set: ").split()

print("The sets are equal" if set_equality(set(set1), set(set2)) else "The sets are not equal")