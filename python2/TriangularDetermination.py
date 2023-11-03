def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        print("It's an equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It's an isosceles triangle.")
    else:
        print("It's a scalene triangle.")

side_1 = float(input("Enter the length of side 1: "))
side_2 = float(input("Enter the length of side 2: "))
side_3 = float(input("Enter the length of side 3: "))

triangle_type(side_1, side_2, side_3)