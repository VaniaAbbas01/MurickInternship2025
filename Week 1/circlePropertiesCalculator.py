import math
import argparse

# Function to calculate area and circumference of a circle given its radius
def calculateCircleProperties(radius):
    try: 
        # calculate area and circumference and round to 2 decimal places
        area = round(math.pi * radius * radius, 2)
        circumference = round(2 * math.pi * radius, 2)
    except: 
        # handle negative radius input
        if radius < 0:
            return "Error: Radius cannot be negative"

    # return area and circumferences
    return area, circumference


if __name__ == "__main__":
    # create argument parser object
    parser = argparse.ArgumentParser(description="Calculate Circle Properties.")

    # defines the radius argument of type float 
    parser.add_argument("radius", type=float, help="The radius of the Circle.")

    # Parses the command-line arguments provided by the user and stores them in the args object
    args = parser.parse_args()

    # access the value of the "radius" argument
    radius = args.radius

    # radius passed to the function
    area, circumference = calculateCircleProperties(radius)

    # print the results
    print(f"The area and circumference of a circle with radius {radius} is: {area:.2f} and {circumference:.2f} respectively.")