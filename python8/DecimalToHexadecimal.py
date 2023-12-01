def decimal_to_hexadecimal(decimal_number):
    hexadecimal_digits = '0123456789ABCDEF'
    hexadecimal_representation = ''

    while decimal_number > 0:
        hexadecimal_digit = decimal_number % 16
        hexadecimal_representation = hexadecimal_digits[hexadecimal_digit] + hexadecimal_representation
        decimal_number = decimal_number // 16

    return hexadecimal_representation

decimal_number = int(input("Enter a decimal number: "))
hexadecimal_representation = decimal_to_hexadecimal(decimal_number)
print("Hexadecimal representation is: ", hexadecimal_representation)