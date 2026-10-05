#Write a python program to rename a file to "renamed_by_python.txt"

with open("09_File_I&O/p.txt") as f:
    content = f.read()

with open("09_File_I&O/renamed_by_python.txt", "w") as f:
    f.write(content)