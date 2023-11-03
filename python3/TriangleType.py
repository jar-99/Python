def triangle_type():
    angle1 = int(input("Enter the first angle: "))
    angle2 = int(input("Enter the second angle: "))
    angle3 = int(input("Enter the third angle: "))

    if angle1 + angle2 + angle3 == 180:  # Checking if the triangle is valid
        if angle1 == angle2 == angle3:
            print("Equilateral triangle")
        elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
            print("Isosceles triangle")
        else:
            print("Scalene triangle")
    else:
        print("Invalid triangle")

triangle_type()