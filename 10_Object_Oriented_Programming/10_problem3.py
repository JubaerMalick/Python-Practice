#Create a class with a class attribute a; create an object from it and set 'a' directly using object.a=o. Does this change the class attribute?

class Demo:
    a = 4


o = Demo()
print(o.a) #Printing the classs attribute because instance attribute is not present

o.a = 0
print(o.a) #Printing the instance attribute beacuse it is present here

print(Demo.a) #It does not changed the Class Attribute