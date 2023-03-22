class C:
    def __init__(self) -> None:
        self.str = str()

    def getString(self):
        self.str = input("Enter a string: ")

    def printString(self):
        print(self.str.upper())


strObj = C()
strObj.getString()
strObj.printString()