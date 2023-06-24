even_count = 0
odd_count = 0

for _ in range(5):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)