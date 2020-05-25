a = [3, 5, 6, 9, 10, 12, 15, 18]
nums_div_by3and5 = [15, 30, 45, 60, 75, 90]
numbers = int(input("Number = " ))

# def addnum(n):
#   new = []
#   for i in range(1, n):
#     if i % 15 == 0:
#       new.append(i)
#     elif i % 3 == 0:
#       new.append(i)
#     elif i % 5 == 0:
#       new.append(i)
#   return new
      
# list_of_nums = addnum(10)
# def sumOfNums(a):
#   total = 0
#   for b in a:
#     total = (total + b)
#   return total

# print(list_of_nums)
# print(sumOfNums(list_of_nums))

def divBy3And5(n):
  total = 0
  for i in range(1, n):
    if i % 3 == 0:
      total += i
    elif i % 5 == 0:
      total += i
  return total

print(divBy3And5(100))
