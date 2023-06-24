def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
even_count = 0
odd_count = 0

for _ in range(5):
    num = int(input("Enter a number: "))
    result = check_even_odd(num)

    if result == "Even":
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
