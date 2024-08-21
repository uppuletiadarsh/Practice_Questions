# polymorphism
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def wheels(self):
        print('4 Wheels')
        print(self.brand)
        print(self.model)
        print(self.year)
class Bike:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def wheels(self):
        print('2 Wheels')
        print(self.brand)
        print(self.model)
        print(self.year)
class Auto:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def wheels(self):
        print('3 Wheels')
        print(self.brand)
        print(self.model)
        print(self.year)
c = Car('Maruthi','zen',2014)
c.wheels()
a = Auto('Tata','magic',2017)
a.wheels()
b = Bike('Hero','splendo',2017)
b.wheels()

for veh in (a,b,c):
    veh.wheels()

# over loading
#operator over loading
print('Adarsh'+'Uppuleti')
print(3 + 5)

class Marks:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,abc):
        print(self.marks + abc.marks)
    def __mul__(self,num):
        print(self.marks * num.marks)
m1 = Marks(60)
m2 = Marks(75)
print(m1 + m2)
m3 = Marks(20)
print(m1*m3)

def sum (a,b):
    return a +b
def sum(x,y):
    return x - y
print(sum(20,10))

# constructor overloading
class Marks:
    def __init__(self,marks):
        self.marks = marks
        print(marks,'Constructor-1')
    def __init__(self,marks):
        self.marks = marks
        print(marks,'constructor-2')
m = Marks(79)

# overriding
class Animal:
    def speak(self):
        print('sound')
class Dog(Animal):
    def speak(self):
        print('bow')
class Cat(Animal):
    def speak(self):
        print('meow')
def sound(animal):
    print(animal.speak())

sound(Dog())  
sound(Cat())  

class Job:
    def adarsh(self):
        print('no skills ,no experience')
    def hire(self):
        print('hire adarsh')
class New(Job):
    def hire(self):
        print('Do not hire')
c = New()
c.hire()

class Iphone:
    def __init__(self,model,price):
        self.model = model
        self.price = price
        print('Constructor-1')
class Iphone:
    def __init__(self,model,price,mp):
        self.model = model
        self.price = price
        self.mp = mp
        print(model,price,mp)
        print('Constructor-2')
c = Iphone('15 pro',80000,60)

class Car:
    def __init__(self,model,price,seats):
        self.model = model
        self.price = price
        self.seats = seats
        print('Car Model:', self.model)
        print('Price:', self.price)
        print('Seats:', self.seats)
        print('constructor-1')

class Car:
    def __init__(self,model,price,seats,breaks):
        self.model = model
        self.price = price
        self.seats = seats
        self.breaks = breaks
        print('Car Model:', self.model)
        print('Price:', self.price)
        print('Seats:', self.seats)
        print('breaks:', self.breaks)
        print('constructor-2')
c = Car('Maaruthi',1000000,4,6)