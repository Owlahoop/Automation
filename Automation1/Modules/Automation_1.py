# When you import a module, that module executable code will run
import PyModule

# This is how to call a module function
PyModule.test_py_mod_fn()

# This is how to call a module function with variables
PyModule.sum_1(5, 10)

# This is how to call a module function with variables and a return
x = PyModule.sum_2(10, 20)
print(x)

# To call anything in a class, need to create an obj of the class
obj = PyModule.A()
obj.testing()