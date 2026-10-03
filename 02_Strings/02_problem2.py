#Write a program to fill in a letter template given below with name and date.
# letter = '''Dear <|Name|>,
# You are selected!
# Date: <|Date|>''' 

letter = '''Dear <|Name|>,
You are selected!
Date: <|Date|>'''

print (letter.replace("<|Name|>", "Jubaer").replace ("<|Date|>", "21 June 2023"))