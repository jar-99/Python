def printCharacterPattern(n):

  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(chr(ord('A') + j - 1), end='')
    print()



n = int(input("Enter the number of rows: "))


printCharacterPattern(n)