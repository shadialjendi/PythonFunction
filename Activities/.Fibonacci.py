def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Main program
limit = int(input("Enter the limit for Fibonacci numbers: "))

# Generate and check Fibonacci numbers
a, b = 0, 1
while a <= limit:
    if not is_prime(a):
        print(a)
    a, b = b, a + b
