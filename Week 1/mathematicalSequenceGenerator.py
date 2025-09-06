# generating fibonacci sequence
def generate_fibonacci(limit):
    fib = [0, 1]
    while fib[-1] + fib[-2] <= limit:
        fib.append(fib[-1] + fib[-2])
    return fib


# generating prime sequence
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes


# generating squares
def generate_squares(limit):
    squares = []
    n = 1
    while n * n <= limit:
        squares.append(n * n)
        n += 1
    return squares


# fibonacci primes sequence
def fibonacci_primes(limit):
    fib = generate_fibonacci(limit)
    primes = generate_primes(limit)
    list_ = []
    for num in fib:
        if num in primes:
            list_.append(num)
    return list_


def menu():
    while True:
        print("\n--- Mathematical Sequence Generator ---")
        print("1. Fibonacci Sequence")
        print("2. Prime Numbers")
        print("3. Perfect Squares")
        print("4. Fibonacci Primes")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            limit = int(input("Enter limit for Fibonacci sequence: "))
            print("Fibonacci sequence:", generate_fibonacci(limit))

        elif choice == "2":
            limit = int(input("Enter limit for prime numbers: "))
            print("Prime numbers:", generate_primes(limit))

        elif choice == "3":
            limit = int(input("Enter limit for perfect squares: "))
            print("Perfect squares:", generate_squares(limit))

        elif choice == "4":
            limit = int(input("Enter limit for Fibonacci primes: "))
            print("Fibonacci primes:", fibonacci_primes(limit))

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


# Run the program
menu()
