#Write a python function to print first n lines of the following patterns:
# ***
# **
# *      for n = 3

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

n = int(input("Enter the no: "))
pattern(n)