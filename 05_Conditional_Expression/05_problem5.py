#Write a program which finds out wheather a given name is present in alist or not.

l = ["Jubaer", "Wasif", "Rifat", "navid"]

name = input("Enter name:")

if (name in l):
    print("Name is present in the list.")

else:
    print("Name is not present in the list.")