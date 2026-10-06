# Write a program to open three files 1.txt, 2.txt, and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.


try:
    with open("13_Advanced_Python_1/1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("13_Advanced_Python_1/2.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("13_Advanced_Python_1/3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)

print("Thank You")