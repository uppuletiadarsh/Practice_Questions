# classes and objects

class Car:
    def __init__(self,name,company):
        self.name = name
        self.company = company
    def drive(self):
        print('the car name is ',self.name,'the company is ',self.company)
c = Car('swift','Maruthi')
c.drive()


class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
    def drive(self):
        print("The engine of the", self.company ,self.model ,"is now running.")
    def details(self):
        print( self.company )
        print( self.model )
        print(self.year)
c = Car("Swift", "dzire", 2024)
c.drive()
c.details()

class Building:
    def __init__(self,colour,shape):
        self.colour = colour
        self.shape = shape 
    def details(self):
        print('the building colour is ',self.colour,'the building shape is ',self.shape)
b = Building('Red','Rectangular')
b.details()
print(b.colour) # accessing by using object reference variable
print(b.shape)

# instance variables
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age   
    def greet(self):
        print("my name is ",self.name ," and i am ",self.age," years old.")
p1 = Person("Adarsh",24)
p2 = Person("Avinesh", 26)
p1.greet()
p2.greet()
print(p1.name)  
print(p2.age)

class Bike:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
    
b = Bike('splendor',100000)
c = Bike('bullet',200000)

print(b.cost)
print(b.name)
Bike.engine = '120cc' # adding from outside of class

print(b.engine)
print(c.engine)

# static varibles

class Car:
    year = 2024
    def __init__(self,company, model):
        self.company = company
        self.model = model

    def details(self):
        print(self.company)
        print(self.model)
        print(Car.year)
c = Car("Toyota", "fortuner")
c.details()
print("year:", Car.year)  
Car.year = 2022
print("Updated year:", Car.year)  

class Employee:
    company = 'Skyawaves'
    count = 0
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id 
        self.salary = salary
        Employee.count = Employee.count + 1
    def detail(self):
        
        print(self.name,'with eid',self.id,'with salary of',self.salary,'working in ',Employee.company,'the employee count is :',Employee.count)
c = Employee('Adarsh',169,26000)
c.detail()
b = Employee('Murali',162,26000)
b.detail()
d = Employee('Chandu',167,26000)
d.detail()

# local variables

class calculator :
    @staticmethod
    def sum1(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
c = calculator()
print(c.sum1(10,20))


class Calculator:
    @staticmethod
    def sum1(a, b):
        return a + b
    @staticmethod
    def sub(a, b):
        return a - b
    @staticmethod
    def mul(a, b):
        return a * b
calc = Calculator()
print(calc.sum1(10, 20))
print(calc.sub(30, 10))
print(calc.mul(5, 6))

class Bike:
    @staticmethod
    def rate():
        print(200000)  
b = Bike()
print(b.rate())


class Building:
    @staticmethod
    def floors():
        print(20)
    @staticmethod
    def rooms():
        print(5)
b = Building()
print(b.floors())
print(b.rooms())