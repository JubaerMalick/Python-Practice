#Write a program using functions to find greatest of three numbers.



def greatest(a, b, c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = 20
b =35
c = 15
print(greatest(a, b, c))