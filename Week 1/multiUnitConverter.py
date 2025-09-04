while True:
    print("Enter a distance")
    distance = float(input())

    print("Enter the unit of the distance entered ")
    print("Options: meters, kilometers, centimeters, millimeters, miles, yards, feet, inches")
    unit = input().lower()

    # Conversion factors to meters
    to_meters = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    }

    if unit not in to_meters:
        print("Invalid unit. Please try again.")
        continue

    print("Enter the unit to convert to ")
    print("Options: meters, kilometers, centimeters, millimeters, miles, yards, feet, inches")
    unit_to = input().lower()

    if unit_to not in to_meters:
        print("Invalid unit. Please try again.")
        continue

    # Convert: input → meters → target
    meters = distance * to_meters[unit]
    converted = meters / to_meters[unit_to]

    print(f"{distance} {unit} is equal to {converted} {unit_to}")

    # Temperature conversion option
    print("Do you want to convert temperature? (yes/no)")
    choice = input().lower()
    if choice == "yes":
        print("Enter a temperature")
        temperature = float(input())
        print("Enter the unit of the temperature entered (celsius, fahrenheit, kelvin)")
        tempUnit = input().lower()

        if tempUnit not in ["celsius", "fahrenheit", "kelvin"]:
            print("Invalid unit. Please try again.")
            continue

        print("Enter the unit to convert to (celsius, fahrenheit, kelvin)")
        tempUnit_to = input().lower()

        if tempUnit_to not in ["celsius", "fahrenheit", "kelvin"]:
            print("Invalid unit. Please try again.")
            continue

        # Temperature conversions
        if tempUnit == "celsius" and tempUnit_to == "kelvin":
            temp_converted = temperature + 273.15
        elif tempUnit == "celsius" and tempUnit_to == "fahrenheit":
            temp_converted = (temperature * 9/5) + 32
        elif tempUnit == "kelvin" and tempUnit_to == "celsius":
            temp_converted = temperature - 273.15
        elif tempUnit == "kelvin" and tempUnit_to == "fahrenheit":
            temp_converted = (temperature - 273.15) * 9/5 + 32
        elif tempUnit == "fahrenheit" and tempUnit_to == "celsius":
            temp_converted = (temperature - 32) * 5/9
        elif tempUnit == "fahrenheit" and tempUnit_to == "kelvin":
            temp_converted = (temperature - 32) * 5/9 + 273.15
        else:
            temp_converted = temperature

        print(f"{temperature} {tempUnit} is equal to {temp_converted} {tempUnit_to}")
    else:
        break

    