# Write executable code first
print("Welcome to the Python Module - PyModule.py")


# Functions inside python file without class, Module Functions
def test_py_mod_fn():
    print("This is a Python Module Function")


def sum_1(a, b):
    print(a + b)


def sum_2(a, b):
    c = a + b
    return c


# Class Functions
class A:
    def __init__(self):
        print("This is Constructor")
    def testing(self):
        print("This is my Class Function")
