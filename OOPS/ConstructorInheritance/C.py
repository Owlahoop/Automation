from A import A

class C(A):
    def __init__(self):
        print("This is C child class constructor")

    def cclassmethod(self):
        print("This is C class method")
