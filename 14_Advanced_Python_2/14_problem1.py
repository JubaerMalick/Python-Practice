# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Jubaer, his marks are 72 and phone number is 99999888"

name = input("Enter name : ")
marks = int(input("Enter marks : "))
phone = int(input("Enter phone no : "))

s = "The name of the student is {}, His mark is {} and phone number is {}".format(name, marks, phone)
print(s)