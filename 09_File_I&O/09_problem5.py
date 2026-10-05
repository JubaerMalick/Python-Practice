#Repeat program 4 for a lilst of such words to be censored.

words = ["Donkey", "bad", "worst"]

with open("09_File_I&O/file2.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#"*len(word))


with open("09_File_I&O/file2.txt", "w") as f:
    f.write(content)