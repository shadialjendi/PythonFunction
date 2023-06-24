#Version 1
number1 = int(input("Please, enter the first number "))
if number1 < 0:
    number1 = 0
number2 = int(input("Please, enter the second number "))
if number2 < 0:
    number2 = 0
number3 = int(input("Please, enter the third number "))
if number3 < 0:
    number3 = 0
print(number1 + number2 + number3)

#Version 2
def CheckPositiveNegative(num):
    if num < 0:
        num = 0
    return num

number1 = CheckPositiveNegative(int(input("Please, enter the first number ")))
number2 = CheckPositiveNegative(int(input("Please, enter the second number ")))
number3 = CheckPositiveNegative(int(input("Please, enter the third number ")))
print(number1 + number2 + number3)