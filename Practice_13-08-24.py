
# instance method 
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

class Car:
    def __init__(self,company, model):
        self.company = company
        self.model = model
    def details(self):
        print("Company: ",self.company,"Model: ",self.model)

c = Car('Maruthi','Zen')
c.details()

class Person:
    def walk(self):
        self.name = 'Adarsh'
        self.dist = 5
        print(self.name,'goes for walk daily',self.dist)
c = Person()
c.walk()

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

# staticmethod

class calculator :
    @staticmethod
    def sum1(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
c = calculator()
c.sum1(10,20)


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
calc.sum1(10, 20)
calc.sub(30, 10)
calc.mul(5, 6)

class Bike:
    @staticmethod
    def rate():
        print(200000)  
b = Bike()
b.rate()


class Building:
    @staticmethod
    def floors():
        print(20)
    @staticmethod
    def rooms():
        print(5)
b = Building()
b.floors()
b.rooms()


#class method
class Car:
    @classmethod
    def describe(cls, brand, model):
        print("car Brand: ",brand,", Model: ",model)
Car.describe("Maruthi", "zen")

class Bus:
    @classmethod
    def describe(cls, capacity,wheels):
        print("Bus Capacity: " ,capacity,"wheels :",wheels)
Bus.describe(50,4)

class Car :
    wheels = 4
    @classmethod
    def m1(cls,name):
        cls.brand = name
        print(cls.brand)
        print(Car.wheels)
v = Car()
v.m1('Maruthi')
print(Car.brand)

class Bike:
    color = 'black'
    @classmethod
    def color(cls,new):
        cls.color = new
    @classmethod
    def m1(cls):
        print(cls.color)
Bike.color('Red')
Bike.m1()
