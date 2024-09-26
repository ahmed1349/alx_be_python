FAHRENHEIT_TO_CELSIUS_FACTOR =5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")

        # Ensure that the input is numeric (including negative temperatures)
        if not temp_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        
        # Ask the user whether the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        
        elif unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
