'''
This code describes the syntax
How you can create the class
How you use create the class attributes
How you can create multiple instances/objects
How you can create methods
'''







class Person:
    def __init__(self, name, age, gender):  # initiator/constructor method
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name} and I am a {self.gender} of {self.age} years old.")

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name



# creating objects/instance of the class
P1 = Person("Esha", 26, "Female")
P2 = Person("Aarav", 15, "Male")

#calling the methods
print(P1.display())
print(P2.display())

#calling the class attributes
print(P1.name)
print(P2.age)

#calling the get/set functions

#get function
print(P1.get_name())
print(P2.get_name())

#set function
print(P2.set_name("Arnav"))

#calling the get function again to show the output changes
print(P2.get_name(),P2.display())