def convert_temperature(temp, unit):
    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
    else :
        converted_temp = (temp - 32) * 5/9
    return converted_temp

# Main program
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

print(convert_temperature(temperature, unit))
