from A import A
from B import B

# Multiple inheritance
class C(A, B):

    def cclassmethod(self):
        print("This is C class method")
