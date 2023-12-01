import math

def quadratic_formula(a, b, c):
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("No real roots")
        return None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        if root1 > root2:
            x1 = round(root1, 2)
            x2 = round(root2, 2)
        else:
            x1 = round(root2, 2)
            x2 = round(root1, 2)
        print("The roots are:", "x1=", x1,"x2=", x2)

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

quadratic_formula(a, b, c)