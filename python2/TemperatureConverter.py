def temperature_converter(temp, unit):
    if unit.upper() == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"Converted temperature: {converted_temp:.2f} F")
    elif unit.upper() == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"Converted temperature: {converted_temp:.2f} C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

temperature_value = float(input("Enter temperature value: "))
temperature_unit = input("Enter unit (C/F): ")

temperature_converter(temperature_value, temperature_unit)