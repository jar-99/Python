def printPattern(rows, columns):
    symbols = ['*', '#']
    for i in range(rows):
        for j in range(columns):
            print(symbols[i%2], end='')
        print()


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))


printPattern (rows , columns)