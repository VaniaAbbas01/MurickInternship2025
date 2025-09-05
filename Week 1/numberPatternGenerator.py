def pattern(start, end, divisor_1, divisor_2, word_1, word_2):
    # Generate pattern
    for num in range(start, end + 1):
        if num % divisor_1 == 0 and num % divisor_2 == 0:
            print(word_1 + word_2)
        elif num % divisor_1 == 0:
            print(word_1)
        elif num % divisor_2 == 0:
            print(word_2)
        else:
            print(num)


while True:
    # Get user input
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    
    divisor1 = int(input("Enter first divisor: "))
    word1 = input("Enter word for first divisor: ")
    
    divisor2 = int(input("Enter second divisor: "))
    word2 = input("Enter word for second divisor: ")

    pattern(start,end,divisor1,divisor2,word1,word2)

    yes_no = input("Do you want to continue? yes/no: ")

    if yes_no.lower() == "no":
        break





