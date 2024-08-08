# functions 
def add (x,y):
    return x + y

def sub(x,y):
    return x - y

def sum_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total
res = sum_list([1, 2, 3, 4, 5])
print(res)  

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
result = factorial(5)
print(result)  

def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total = total + num
    return total
res = sum_range(1, 5)
print(res)  
