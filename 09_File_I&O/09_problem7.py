#Write a program to find out the line number where python is present from P:6

with open("09_File_I&O/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("Python" in line):
        print(f"Yes Python is present. Line no: {lineno}")
        break
    lineno += 1


else:
    print("No Python is not present")