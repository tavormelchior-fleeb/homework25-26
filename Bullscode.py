from random import randint


class BullsCode:
    def __init__(self, value=randint(1000, 9999)):
        self.value = value

    def __str__(self):
        return f"the value is {self.value}"

    def getvalue(self):
        return self.value

    def setvalue(self):
        return self.value


