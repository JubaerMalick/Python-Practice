#Write a program to find out wheather a file is identical & matches the content of another file.

with open("09_File_I&O/ident1.txt") as f:
    content1 = f.read()

with open("09_File_I&O/ident2.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these files are identical.")

else:
    print("No these files are not identical")