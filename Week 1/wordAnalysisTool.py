import argparse
import string

# Function to analyze a word
def totalCharacters(word):
    count = 0
    # to prevent counting spaces
    for char in word:
        if char != " ":
            count += 1
    return count

# Function to count total words in a sentence
def totalWords(word):
    words = word.split()
    return len(words)

# Function to count total vowels in a word
def totalVowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Function to count total consonants in a word
def totalConsonants(word):
    vowels = "aeiouAEIOU"
    count = 0
    # iterating through each character in the word
    for char in word:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

# Function to find the longest word in a sentence
def longestWord(word):
    words = word.split()
    # handle empty string case
    if not words:
        return ""
    # return the word with maximum length
    longest = max(words, key=len)
    return longest

if __name__ == "__main__":
    # create argument parser object
    parser = argparse.ArgumentParser(description="Analysing a Word.")

    # defines the sentence argument of type float 
    parser.add_argument("sentence", type=str, help="The sentence to be analysed.")

    # Parses the command-line arguments provided by the user and stores them in the args object
    args = parser.parse_args()

    # access the value of the "radius" argument
    sentence = args.sentence

    try: 
        # sentence passed to the function
        characters = totalCharacters(sentence)
        words = totalWords(sentence)
        vowels = totalVowels(sentence)
        consonants = totalConsonants(sentence)
        longest = longestWord(sentence)

        # print the results
        print(f"Total Characters: {characters}")
        print(f"Total Words: {words}")
        print(f"Total Vowels: {vowels}")
        print(f"Total Consonants: {consonants}")
        print(f"Longest Word: {longest}")
        

    except TypeError:
        print("Error: Invalid input")
        exit()