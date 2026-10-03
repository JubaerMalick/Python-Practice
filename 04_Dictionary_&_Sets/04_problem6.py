#Create an empty dictionary. Allow 4 friends to enter their favourite languages as value and use key as their names. assume that the names are unique.

d ={}

name = input("Enter name:")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name:")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name:")
lang = input("Enter language: ")
d.update({name : lang})

name = input("Enter name:")
lang = input("Enter language: ")
d.update({name : lang})

print (d)