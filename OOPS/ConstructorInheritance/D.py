from C import C
from A import A

# C class constructor will be the only one called
obj = C()
# Must create object of parent to call parent constructor
obj1 = A()
obj.cclassmethod()
obj.aclassmethod()
