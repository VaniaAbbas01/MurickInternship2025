from collections import Counter

# Check if two words are anagrams
def is_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())

# Find all anagrams of a word from a list
def find_anagrams(word, word_list):
    sorted_word = sorted(word.lower())
    list_ = []
    for w in word_list:
        if sorted(w.lower()) == sorted_word and w.lower() != word.lower():
            list_.append(w)
    return list_

# Edit distance (for spell checking)
def edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    print(dp)
    return dp[n][m]

def spell_check(word, dictionary):
    scores = [(w, edit_distance(word, w)) for w in dictionary]
    scores.sort(key=lambda x: x[1])
    return scores[:3]   # top 3 suggestions

# --- 4) Longest Common Subsequence ---
def lcs(a, b):
    n, m = len(a), len(b)
    dp = [[""]*(m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + a[i]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
    return dp[n][m]

# --- Menu Program ---
if __name__ == "__main__":
    while True:
        print("\n--- Text Pattern Analyzer ---")
        print("1. Check Anagrams")
        print("2. Find Anagrams from List")
        print("3. Spell Checker")
        print("4. Longest Common Subsequence")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            w1 = input("Enter first word: ")
            w2 = input("Enter second word: ")
            print("Anagrams?" , is_anagram(w1, w2))

        elif choice == "2":
            word = input("Enter word: ")
            words = input("Enter word list (comma separated): ").split(",")
            print("Anagrams found:", find_anagrams(word, words))

        elif choice == "3":
            word = input("Enter word to check: ")
            dictionary = input("Enter dictionary words (comma separated): ").split(",")
            print("Suggestions:", spell_check(word, dictionary))

        elif choice == "4":
            a = input("Enter first string: ")
            b = input("Enter second string: ")
            print("Longest Common Subsequence:", lcs(a, b))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")
