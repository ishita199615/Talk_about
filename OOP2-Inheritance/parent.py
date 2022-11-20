class Parent:
    name: object

    def __init__(self, name: object):
        """

        :type name: object
        """
        self.main = None
        self.name = name

    # method
    def display(self):
        return f"My name is {self.name}"

