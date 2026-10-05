##Write a program to read text from a given file ""poem.txt" and find out wheather it contains the word "twinkle"

f = open("09_File_I&O/poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present.")
else:
    print("twinkle not present.")

f.close()