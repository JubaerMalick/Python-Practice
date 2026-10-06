#Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce 

a = [1, 5, 10, 7, 75, 55, 57, 47, 65]

def greater(a, b):
    if (a>b):
        return a
    return b

print(reduce(greater, a))