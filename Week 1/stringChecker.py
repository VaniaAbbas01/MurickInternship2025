import math

# removes special characters and empty spaces from string
def cleanString(string):
    string = string.lower()
    special_char = "-/?.,;:_=+&^%$#@!*~`"
    newString = ""
    for char in string:
        if char != " " and char not in special_char:
            newString += char
    return newString

# checks for palindrome
def checkPalindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return "A Palindrome" 
    return "Not a Plaindrome"

# checks if string contains alphabets only or numbers as well
def checkAlphabetic(text):
    if text.isalpha():
        return "Contains only alphabetic characters"
    else:
        return "Contains alphanumeric or special characters"

# checks balance of parenthesis
def checkBalancedParenthesis(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "Parentheses are NOT balanced"
            stack.pop()
    if not stack:
        return "Parentheses are balanced" 
    return "Parentheses are NOT balanced"

while True:
    string = input("Enter a string: ")
    cleaned = cleanString(string)
    print("Cleaned string:", cleaned)

    print(checkPalindrome(cleaned))
    print(checkAlphabetic(cleaned))
    print(checkBalancedParenthesis(string))

    again = input("Do you want to check another string? (yes/no): ")
    if again.lower() == "no":
        print("Exiting program.")
        break
