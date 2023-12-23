def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("1. Temperature Converter\n2. Length Converter\n3. Weight Converter")

    choice = input("Enter the number corresponding to the converter type: ")

    if choice == "1":
        temperature_converter()
    elif choice == "2":
        length_converter()
    elif choice == "3":
        weight_converter()
    else:
        print("Invalid choice. Please enter a valid option.")

def temperature_converter():
    source_unit = input("Enter the source temperature unit (Celsius or Fahrenheit): ").lower()
    target_unit = input("Enter the target temperature unit (Celsius or Fahrenheit): ").lower()

    try:
        value = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    if source_unit == "celsius" and target_unit == "fahrenheit":
        result = celsius_to_fahrenheit(value)
    elif source_unit == "fahrenheit" and target_unit == "celsius":
        result = fahrenheit_to_celsius(value)
    else:
        print("Unsupported units for temperature conversion.")
        return

    print(f"Result: {value} {source_unit} is {result:.2f} {target_unit}.")

# Similar functions for length_converter() and weight_converter().

if __name__ == "__main__":
    unit_converter()
