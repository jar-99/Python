character = input("Enter a character: ")

if character.isdigit() and len(character) == 1:
    print("The character is a digit.")
else:
    print("The character is not a digit.")
