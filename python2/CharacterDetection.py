def character_detector(char):
    if char.isalpha():
        if char.lower() in 'aeiou':
            print("The character is a vowel.")
        else:
            print("The character is a consonant.")
    elif char.isdigit():
        print("The character is a digit.")
    elif char.islower():
        print("The character is a lowercase letter.")
    elif char.isupper():
        print("The character is an uppercase letter.")
    else:
        print("The character is not a letter or a digit.")

character = input("Enter a character: ")

if len(character) == 1:
    character_detector(character)
else:
    print("Please enter only one character.")