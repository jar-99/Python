def countWords(sentence):

    words = sentence.split()

    return len(words)

sentence = input("Enter a sentence: " + "")
print("Number of words:", countWords(sentence))