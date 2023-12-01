def vowelReplacer():
    sentence = input("Enter a sentence: ")
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        sentence = sentence.replace(vowel, "x")
    return sentence

modifiedString = vowelReplacer()
print(modifiedString)