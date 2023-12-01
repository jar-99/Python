def oppCase(char):
  if char.islower():
    return char.upper()
  else:
    return char.lower()

def main():
  char = input("Enter a character: ")
  result = oppCase(char)
  print(result)

if __name__ == "__main__":
  main()