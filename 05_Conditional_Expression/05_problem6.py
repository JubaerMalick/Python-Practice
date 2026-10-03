#Write a program to calculate the grade of a student from his marks.

marks = int(input("Enter your marks:"))

if (marks<=100 and marks>=90):
    print("Your grade is Ex")

if (marks<90 and marks>=80):
    print("Your grade is A")

if (marks<80 and marks>=70):
    print("Your grade is B")

if (marks<70 and marks>=60):
    print("Your grade is C")

if (marks<60 and marks>=50):
    print("Your grade is D")

if (marks<50):
    print("Your grade is F")

