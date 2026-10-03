#Write a program to find wheather a given number is prime or no.

n = int(input("Enter a number: "))

for i in range (2, n):
    if(n%2) == 0:
        print("Number is not prime")
        break
else:
    print("Number is Prime")