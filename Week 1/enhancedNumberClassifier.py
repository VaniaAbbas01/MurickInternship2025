import math
import argparse

# check if number is even or odd
def checkEvenOdd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# check if number is positive, negative or zero
def checkPositiveNegative(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
    
# check if number is a perfect square
def checkPerfectSquare(number):
    if number < 0:
        return "Negative numbers cannot be perfect squares"
    root = math.isqrt(number)
    if root * root == number:
        return "Perfect Square"
    else:
        return "Not a Perfect Square"
    
# check if number is a power of two
def checkNumberPowerOfTwo(number):
    if number <= 0:
        return "Not a Power of Two"
    elif (number & (number - 1)) == 0:
        return "Power of Two" 
    else:
        return "Not a Power of Two"
    

if __name__ == "__main__":
    # create argument parser object
    parser = argparse.ArgumentParser(description="Classifying a Number.")

    # defines the number of type float
    parser.add_argument("number", type=int, help="The number.")

    # Parses the command-line arguments provided by the user and stores them in the args object
    args = parser.parse_args()

    # access the value of the "number" argument
    number = args.number

    try: 
        # classifying the number
        even_odd = checkEvenOdd(number)
        pos_neg = checkPositiveNegative(number)
        perfect_square = checkPerfectSquare(number)
        power_of_two = checkNumberPowerOfTwo(number)

        # print the results
        print(f"The number {number} is classified as:")
        print(f"1. {even_odd}")
        print(f"2. {pos_neg}")      
        print(f"3. {perfect_square}")
        print(f"4. {power_of_two}")

    except TypeError:
        print("Error: Invalid input")
        exit()

