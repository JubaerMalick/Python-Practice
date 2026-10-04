#Write a python function to remove given word from a list ad strip it "if" the same time.

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Jubaer", "Wasif", "Jarif", "Asif", "Rahim"]
print(rem(l, "if"))