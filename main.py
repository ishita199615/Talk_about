# import modules
# from parent import *
# from child import *
# from single_Inheritance import *
from multilevel_inheritance import *
from multiple_inheritance import *

# module_name.class_name --> this can also be used when creating an object

# calling parent class function
# obj1 = Parent('ABC')
# print(obj1.display())

# main class driver
# dir(obj1.main)

# Calling child class function
# obj2 = Child('XYZ')
# print(obj2.print1())
# print('---------------')
# print('---------------')
# --------------------------------

# calling  single-inheritance base class

#  calling super-class
# person1 = BaseClass('Tina', 'PQR')
# person1 = person1.company
# print(person1)

# calling sub class
# person2 = DeriveClass('Elina', 'XYZ', 'Data Scientist', 10)
# person2 = person2.company
# print(person2)

# ------------------------------------

# calling  multilevel-inheritance base class

#  calling super-class
# person4 = BaseClass('Tina', 'PQR')
# person4 = person4.company
# print(person4)

# calling sub class
# 'Elina', 'XYZ', 'Data Scientist', '70k', 10, 'yes'
person5 = DeriveClass2('Elina', 'XYZ', 'Data Scientist', '70k', 10, 'yes')
# print(person5.compensation)
print(person5)
