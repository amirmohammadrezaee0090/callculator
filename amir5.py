def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Get input from the user
terms = int(input("Enter the number of Fibonacci terms to generate: "))

if terms <= 0:
    print("Number of terms should be greater than zero.")
else:
    fibonacci_sequence = generate_fibonacci(terms)
    print("Fibonacci Sequence:")
    print(fibonacci_sequence)
