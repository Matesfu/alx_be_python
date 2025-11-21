FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
try:
    temperature = float(input("Enter the temperature to convert: "))
except:
    print("you should enter number on the place of temperature!!")
    exit()

conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if conversion.lower() == "c":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif conversion.lower() == "f":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
else:
    print("put proper conversion unit!!")