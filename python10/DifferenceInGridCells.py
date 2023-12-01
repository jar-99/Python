def printGridPattern(rows, columns):

  for i in range(rows):
    for j in range(columns):
      difference = i - j
      print(difference, end=' ')
    print()



rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


printGridPattern(rows, columns)