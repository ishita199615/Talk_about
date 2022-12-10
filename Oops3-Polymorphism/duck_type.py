#Duck Type Polymorphism

class Parent:
    def execute(self):
        print('Compiling')
        print('yeahh,running!!')


class Editor:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("running")

#Here you can use the method defined as above
class Laptop:
    def code(self, idle):
        idle.execute()