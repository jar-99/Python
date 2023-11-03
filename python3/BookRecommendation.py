def recommend_book(age, genre):
    if 8 <= age <= 12:
        if genre == 'a':
            print("The Adventures of Tom Sawyer")
        elif genre == 'm':
            print("Nancy Drew: The Secret of the Old Clock")
        else:
            print("No recommendation available")
    elif age >= 13:
        if genre == 'f':
            print("Harry Potter and the Sorcerer's Stone")
        elif genre == 's':
            print("Ender's Game")
        else:
            print("No recommendation available")
    else:
        print("No recommendation available")

age = int(input("Enter your age: "))
genre = input("Enter your genre preference (a for adventure, m for mystery, f for fantasy, s for science fiction): ")

recommend_book(age, genre)