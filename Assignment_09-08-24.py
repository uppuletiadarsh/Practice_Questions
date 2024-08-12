"""
1.Write a program which can filter even numbers in a list by using filter function. The list is: 
[1,2,3,4,5,6,7,8,9,10].

"""

# using Function()
list1 = [1,2,3,4,5,6,7,8,9,10]
def Even_filter(x):
    if x % 2 == 0:
        return x
Even_list = list(filter(Even_filter,list1))
print('Original List :',list1)
print('The Even List :',Even_list)


# using Lamda function
list1 = [1,2,3,4,5,6,7,8,9,10]
Even = lambda x: x if x%2 == 0 else False
Even_list = list(filter(Even,list1))
print('Original List :',list1)
print('The Even List :',Even_list)


"""
2. Write a program which can map() to make a list whose elements are square of elements in 
[1,2,3,4,5,6,7,8,9,10].

"""

list1 = [1,2,3,4,5,6,7,8,9,10]
def Square_filter(x):
    return x*x
square_list = list(map(Square_filter,list1))
print('Original List :',list1)
print('The Squre List :',square_list)

# using Lamda function
list1 = [1,2,3,4,5,6,7,8,9,10]
Square = lambda x: x*x
square_list = list(map(Square,list1))
print('Original List :',list1)
print('The Squre List :',square_list)

"""
3. Write a program which can map() and filter() to make a list whose elements are square of even 
number in [1,2,3,4,5,6,7,8,9,10].
"""

# using Regular Function
list1 = [1,2,3,4,5,6,7,8,9,10]
def Even(x):
    if x % 2 == 0:
        return x
def Square(x):
    return x*x
Even_filter = list(filter(Even,list1))
Even_Square = list(map(Square,Even_filter))
print(Even_Square)

# Using Lamda
list1 = [1,2,3,4,5,6,7,8,9,10]
Even = lambda x : x if x %2 ==0 else False
Square = lambda x : x*x
Even_filter = list(filter(Even,list1))
Even_Square = list(map(Square,Even_filter))
print(Even_Square)

"""
4. Write a program which can filter() to make a list whose elements are even number between 1 and 
20 (both included)
"""
# using regular function
list1 = list(range(1,21))
def Even_filter(x):
    if x % 2 == 0:
        return x
Even_list = list(filter(Even_filter,list1))
print('Original List :',list1)
print('The Even List :',Even_list)

# using lambda
list1 = list(range(1,21))
Even = lambda x: x if x%2 == 0 else False
Even_list = list(filter(Even,list1))
print('Original List :',list1)
print('The Even List :',Even_list)

'''
5. Write a program which can map() to make a list whose elements are square of numbers between 
1 and 20 (both included).
'''

# using regular Function
list1 = list(range(1,21))
def Even(x):
    if x % 2 == 0:
        return x
def Square(x):
    return x*x
Even_filter = list(filter(Even,list1))
Even_Square = list(map(Square,Even_filter))
print(Even_Square)

# using Lambda
list1 = range(1,21)
Even = lambda x : x if x %2 ==0 else False
Square = lambda x : x*x
Even_filter = list(filter(Even,list1))
Even_Square = list(map(Square,Even_filter))
print(Even_Square)


# 6. Define a class named American and its subclass NewYorker
class American :
    def __init__(self,name,domain,salary):
        self.name = name
        self.domain = domain
        self.salary = salary
    def details1(self):
        print('The Employee name is ',self.name,'Domain is ',self.domain,' And the Salary is ',self.salary)
class NewYorker(American):
    def __init__(self,name,domain,salary,company):
        super().__init__(name,domain,salary)
        self.company = company
    def details2(self):
        print('The Employee name is ',self.name,'Domain is ',self.domain,' And the Salary is ',self.salary,'in',self.company,'Company')

det = NewYorker('Adarsh','Python',30000,'Skywaves Pvt Ltd')
det.details1()
det.details2()


"""
7. Define a class named Rectangle which can be constructed by a length and width. The Rectangle 
class has a method which can compute the area.
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def Area(self):
        print('Length :',self.length)
        print('Breadth :',self.breadth)
        print('The Area of Rectangle is :',2*self.length*self.breadth)
l = input('Enter the Length of Rectangle :')
b = input('Enter the Breadth of Rectangle :')
if l.isdigit() and b.isdigit():
    a = Rectangle(int(l),int(b))
    a.Area()
else:
    print('Enter Proper Digits')


"""
8. Write a function that returns the lesser of two given numbers if both numbers are even, but 
returns the greater if one or both numbers are odd
"""
def Function_1(x,y):
    if x % 2 == 0 and y % 2 ==0 :
         return min(x,y)
    else:
        return max(x,y)
print(Function_1(9,8))



# 9. Write a function takes a two-word string and returns True if both words begin with same letter
string = input('Enter the 2-word string: ')
def compare(x):
    words = x.split()
    if len(words) == 2:
        first = words[0][0]
        second = words[1][0]
        if first.lower() == second.lower():
            print('Starting letters of both words are the same and it is True')
        else:
            print('Starting letters of both words are not the same and it is False')
    else:
        print('Enter only 2 words')
compare(string)


## 10. Write a function that capitalizes the first and fourth letters of a name
def Capital_first4(x):
    New_name = ''
    if x == ' ' or x =='' :
        print('Enter Proper Name')
    elif len(x) > 4 :
        first_four = str(x[0:4]).upper()
        remain  = str(x[4:]).lower()
        New_name=first_four +remain
    elif len(x) < 4 :
        first_four = str(x[0:]).upper()
        New_name = New_name + first_four
    print(New_name)
Name = input('Enter the Name : ')
Capital_first4(Name)




