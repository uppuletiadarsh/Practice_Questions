# random module
import random
import random


b = random.randint(1, 10)
print(b)  

import random
li = ['apple', 'banana', 'cherry']
a = random.choice(li)
print(a)  

for i in range(10):
    print(random.randint(1, 10))

# math module

import math
a = math.sqrt(16)
print(a)  

b = math.pow(2, 3)
print(b)  

g = math.factorial(5)
print(g)  

# ceil() above near integer value
j = math.ceil(4.2)
print(j)  

# floor() below near integer value
k = math.floor(4.7)
print(k)  


# date time module

import datetime


from datetime import time

t = time(15, 30, 45)
print(t)  


dt = datetime.datetime.now()
print(dt)  

today = datetime.date.today()
print(today)  

#calender module
import calendar
cal = calendar.month(2024,8)
print(cal)