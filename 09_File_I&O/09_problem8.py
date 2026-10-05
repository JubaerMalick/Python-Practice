#Write a program to make a copy of a text file "this.txt"

with open("09_File_I&O/this.txt") as f:
    content = f.read()

with open("09_File_I&O/this_copy.txt", "w") as f:
    f.write(content)