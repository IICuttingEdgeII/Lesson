import _sqlite3

# User input
# name = input("What is your name?")
# print(name)
# age = int(input("What is your age?"))
# print(age)

# Mathematical Operators
x = 5
y = 3
print(x + y)
print(x - y)
print(x / y)
print(x * y)
# to the power of
print(x ** y)
# modulus - the remainder
print(x % y)


def isLeapYear(year):
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not leap year")


# Floor division (div)
print(x // y)
# Greater Than, Less than, Equal To
print(x > y)
print(x < y)
print(x == y)
print(3 >= 3)
print(5 <= 3)
x = 5.64
print(int(x))


def divisibleby5(n):
    numbers = []
    for i in range(1, n + 1):
        if i % 5 == 0:
            numbers.append(i)
    return numbers


def subtract1(numbers):
    new = []
    for i in numbers:
        new.append(i-1)
    return new

numbers = divisibleby5(100)
minus1 = subtract1(numbers)
print(numbers)
print(minus1)

people = {"Bob":3, "C":5, "D":6}
print(people.get("Bob"))
people["G"] = 1
print(people)
print(people.keys())
print(people.values())
print(people.items())