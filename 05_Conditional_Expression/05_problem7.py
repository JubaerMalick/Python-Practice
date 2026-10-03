#Write a program to find out wheather a given post is talking about "Jubaer" or not.

post = input("Enter post:")

if ("Jubaer".lower() in post.lower()):
    print("The post is about Jubaer.")

else:
    print("The post is not about Jubaer.")