# recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)  
print(result)

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
res = sum(5)  
print(res)

# lamda function
add = lambda x,y : x+y
print(add(10,20))

cond = lambda x,y: x if x>y else y
print(cond(300,200))

# iterations
# map()
l = [1,2,3,4,5,6,7]
def add(x):
    return x + 1
new = list(map(add,l))
print(new)

l = [1,2,3,4,5,6,7]
add = lambda x:x+10
new = list(map(add,l))
print(new)


# filter()
l = [1,2,3,4,5,6,7]
def fil(x):
   if x%2==0:
       return x
new = list(filter(fil,l))
print(new)

l = [1,2,3,4,5,6,7]
fil = lambda x:x if x%2==0 else False
new = list(filter(fil,l))
print(new)


# reduce()
from functools import *
l = [1,2,3,4,5,6,7]
sum = sum(l)
print(sum)

def sum(x,y):
    return x + y
def_sum = reduce(sum,l)
print(def_sum)

l = [1,2,3,4,5,6,7]
add = lambda x,y:x+y
new = reduce(add,l)
print(new)
