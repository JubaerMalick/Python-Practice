#Store the multiplication tables generated in problem 3 in a file named Tables.txt

n = int(input("Entyer a number : "))

table = [n*i for i in range(1, 11)]
print(table)

with open("13_Advanced_Python_1/tables.txt", "a") as f:
    f.write(f"Table of {n} : {str(table)} \n")