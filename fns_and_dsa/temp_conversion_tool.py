FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):

    celcius_temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celcius_temperature}°C")

def convert_to_fahrenheit(celsius):

    farenheit_temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°F is {farenheit_temperature}°C")

temperature = float(input("Enter the temperature to convert: "))
scale_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if (scale_unit == "F"):
    convert_to_celsius(temperature)
elif (scale_unit == "C"):
    convert_to_fahrenheit(temperature)
else:
    print("Invalid temperature. Please enter a numeric value.")
    
