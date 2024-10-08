# importing module
import module0

#importing modules from package
from package_1 import module_1,module_2

print(module0.greet("Jayant"))
print(module0.pi)


print(module_1.function1())
print(module_2.function2())


# import math               # importing as a namespace
# from math import *        # importing everything in current namespace, so not recommended
# from math import sqrt, pi # Import specific functions
