#homework1
#Due 10/10/18

# Problem 1
#Write a Python program to count the number
#of even and odd numbers from a series of numbers.
#Be sure to print out what numbers are even and what numbers are odd.
#(Hint use a for loop)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
countOdd = 0
countEven = 0
for x in numbers:
  if x % 2 == 0:
    countEven+=1
  else:
    countOdd+=1
print("There are ", countEven, "even numbers")
print("There are", countOdd, "odd numbers")

for x in numbers:
  if x % 2 == 0:
    print(x, "is even")
  else:
    print(x, "is odd")
