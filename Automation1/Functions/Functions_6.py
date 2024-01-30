# Required Arguments
def take_input_1(a, b):
    # a and b are required arguments
    c = a + b
    print("Sum of values " + str(c))


# Keyword Arguments
def take_input_2(a, b):
    c = a - b
    print("Difference of values " + str(c))


# Default Arguments
def take_input_3(a, b=10):
    # b can be overwritten, defaults must be defined as last variables
    c = a + b
    print("Sum of values " + str(c))


take_input_1(10, 30)
take_input_2(b=500, a=100)  # Keyword argument
take_input_3(20)
