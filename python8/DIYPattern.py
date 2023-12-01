def print_pattern(n1, n2, n3, n4):
   pattern = []

   pattern.append(" ".join(n1*["#"]))
   pattern.append(" ".join(n2*["|"]))
   pattern.append(" ".join(n3*["/"]))
   pattern.append(" ".join(n4*["_"]))
   print("\n".join(pattern))


n1 = int(input("Enter the value of n1: "))
n2 = int(input("Enter the value of n2: "))
n3 = int(input("Enter the value of n3: "))
n4 = int(input("Enter the value of n4: "))


if n1 < n3 or n2 <= 0 or n3 <= 0 or n4 <= 0:
   print("Invalid input. Please ensure all values are positive integers and n1 >= n3.")
else:
   print_pattern(n1, n2, n3, n4)