#Write a program to calculate the factorial of given numbers using for loop.

n = int(input("Enter the number: "))
product = 1

for i in range(1, n+1):
    product *= i

print (f"The factorial of {n} is : {product}")
