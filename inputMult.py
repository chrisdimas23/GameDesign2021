# Chris Dimas
# 6/4/2021
# We are going to print multiplication tables
# Using print statements and a variable
# input - - - > from the User
# Use the funtion input()
# variables need to have a valid name
print("enter a number")
base=int(input())
print(base)

for counter2 in range(1,11):   #intital value included and ending value that is not included
            print(base, "x", counter2, "=", counter2 * base)