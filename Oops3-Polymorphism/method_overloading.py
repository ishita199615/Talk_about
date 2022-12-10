'''
class Calculate:
    @staticmethod
    def add(a1, a2):
        total = a1+a2
        return  total

    def add(self,a1,a2,a3):
        total = a1+a2+a3
        return total
'''

'''
from multipledispatch import dispatch
class Calculate1:
    @dispatch(int , int)
    def add(self,a1,a2):
        return a1+a2

    @dispatch(float,float,int)
    def add(self,a1,a2,a3):
        return a1+a2+a3

    @dispatch(str,str)
    def add(self,a1,a2):
        return a1+a2
'''
'''
class Calculate2:
    a1, a2, a3 = 0, 0, 0

    @staticmethod
    def add(a1, a2):
        total = a1 + a2
        return total

    @staticmethod
    def add(a1, a2=None, a3=None):
        if a3 is not None or a2 is not None:
            total = a1 + a2 + a3
            return total
        elif a1:
            total = a1
            return total
'''

'''
# Below code will raise error
class Calculate2:
    a1, a2, a3 = 0, 0, 0

    @staticmethod
    def add(a1, a2):
        total = a1 + a2
        return total

    @staticmethod
    def add(a1, a2=None, a3=None):
        total = a1 + a2 + a3
        return total
'''