def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit == 'C':
    converted_temp = celsius_to_fahrenheit(temperature)
else :
    converted_temp = fahrenheit_to_celsius(temperature)

print("The converted temparature is", converted_temp)