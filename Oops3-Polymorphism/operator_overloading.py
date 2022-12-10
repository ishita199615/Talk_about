'''
class Oper1:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2

    def __add__(self, other):
        a1 = self.a1 + other.a1
        a2 = self.a2 + other.a2
        a3 = a1+a2
        return a3

    def __gt__(self, o):
        a4 = self.a1 + o.a1
        a5 = self.a2 + o.a2
        if a4>a5:
            return True
        else:
            return False

    def __invert__(self,other):
        a1 = self.a1 + other.a1
        a2 = self.a2 + other.a2
        a3 = a1+a2
        return a3
'''

class A:
    def __init__(self, a):
        self.a = a

    # Overloading ~ operator, but with two operands
    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator."


ob1 = A(2)

print(~ob1)