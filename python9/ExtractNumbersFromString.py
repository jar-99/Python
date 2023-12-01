def extract_numbers(string):
    numbers = ''
    for char in string:
        if char.isdigit():
            numbers += char
    return numbers

input_string = input("Enter a string: ")
extracted_numbers = extract_numbers(input_string)

print(f"The extracted numbers are: {extracted_numbers}")