class Parent:
    @property
    def f1(self):
        return 'My child is in Grade 2'


class Child(Parent):
    @property
    def f1(self):
        return "Next year, I will be going to Grade 3"
