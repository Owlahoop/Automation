class A:
    def __init__(self, a, b):
        print("This is a constructor")
        c = a + b
        print(c)

    # Function with no argument, and no return value
    def hello(self):
        print("Hello World")

    # Function with argument, but no return value
    def sum_1(self, a, b):
        c = a + b
        print("Sum is " + str(c))

    # Function with argument, and return value
    def mul_1(self, a, b):
        c = a * b
        return c


obj = A(5, 4)
obj.hello()
obj.sum_1(10, 20)
x = obj.mul_1(2, 10)
print(x)
