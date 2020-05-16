# selection
person = "ob"
if person[0] == "B":
    print("First letter is B")
# loops
cities = ["London", "New York", "Tokyo"]
for a in cities:
    print(a)
for n in range(1, 101):
    print(n)

n = 1
while n < 101:
    print(n)
    n += 1

# String methods
a = "Japan"
a = a.lower()
print(a)
a = a.upper()
print(a)
a = a.title()
print(a)
a = a[::-1]
print(a)

# List methods
cities = ["London", "New York", "Tokyo", "Chennai"]
cities.reverse()
print(cities)

first = ["A", "B", "C"]
last = ["Z", "Y", "X"]
for i in range(len(first)):
    n = first[i] + " " + last[i]
    print(n)

# list append
numbers = []
for i in range(1, 11):
    numbers.append(i)
print(numbers)