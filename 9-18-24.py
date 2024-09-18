#  =======================================MODULES========================================
'''
>>> collections of functions, class, variables
>>> python files, having .py extension
>>> this helps in organizing code into manageable and reuseable components
'''


# inbuilt modules
import os
import math
print(dir(math)) # prints all the math functions 
import datetime
import random

# custom modules
'''
>>> we can customize our modules based on requierment
>>> we can import customized modules into another module
'''

# third party modules >>> requests, pandas

import random # >>> it generates random numbers
print(random.randint(1,100)) 
print(random.random()) #>>> generates random flout value


for i in range (10):
    print(random.randint(1,100))

for i in range (10):
    print(random.random())

l=["ram","shyam","hari","giri","sai"]
for i in range(3):
    print(random.choice(l))