# Write a program to greet all the person names stored in a list 'l' and which starts with J and W.

l = ["Jubaer", "Tom", "Alice", "Bob", "Wasif"]

for name in l:
    if(name.startswith("J") or name.startswith("W")):
        print(f"Hello {name}")