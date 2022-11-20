from parent import Parent


# This Child class will adapt everything from parent class
# You can also create your own methods in child class

class Child(Parent):

    def print1(self):
        return f'Child class called and my name is {self.name}'







