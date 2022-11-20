class BaseClass:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    # Getter and Setter methods
    @property  # decorator
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    # magic methods
    def __str__(self):
        return f'My name is {self.name}.\nI work in {self.company} company'


# Sub-Class/Child-Class/Derive-Class
class DeriveClass(BaseClass):

    def __init__(self, name, company, position, exp=int):
        self.position = position
        self.exp = exp

        # initializing the Super class
        BaseClass.__init__(self, name, company)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, exp):
        self.__exp = exp

    # magic method inheritance
    def __str__(self):
        return super().__str__() + '.' + f' My current position is {self.position} and experience is {self.exp}'


# Multi-class level inheritance

class DeriveClass2(DeriveClass):
    def __init__(self, name, company, position, compensation,  promotion, exp=int) -> object:
        """

        :rtype: object
        """
        self.compensation = compensation
        self.promotion = promotion

        DeriveClass.__init__(self, name, company, position, exp)

    # Getter and Setter Methods
    @property
    def compensation(self):
        return self.__compensation

    @compensation.setter
    def compensation(self, compensation):
        self.__compensation = compensation

    @property
    def promotion(self):
        return self.__promotion

    @promotion.setter
    def promotion(self, promotion):
        self.__promotion = promotion

    def __str__(self):
        return super().__str__() + "." + f' My base compensation is {self.compensation}.\n{self.promotion}, last year I was ' \
                                         f'promoted. '


# Mutli-level inheritance
class FinalClass(DeriveClass2):
    def __str__(self):
        return super().__str__()
