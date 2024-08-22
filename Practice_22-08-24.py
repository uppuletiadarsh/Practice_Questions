# abstraction-------------------------------------------------------------------------
from abc import ABC,abstractmethod
class Work(ABC):
    @abstractmethod
    def m1(self):
        pass
class Office(ABC):
    def m1(self):
        pass
class Manager(Office):
    def m1(self):
        print('Manager')
class lead(Office):
    def m1(self):
        print('lead')
class developer(Office):
    def m1(self):
        print('developer')
o = Office()
o.m1()
m= Manager()
m.m1()
l = lead()
l.m1()
d = developer()
d.m1()
#------------------------------------------------------------------------------
class Department(ABC):
    @abstractmethod
    def name(self):
        pass
class HR(Department):
    def name(self):
        print('hr')

class IT(Department):
    def name(self):
        print('it')
class Design(Department):
    def name(self):
        print('design')

class QA(Department):
    def name(self):
        print('testing')

class Finance(Department):
    def name(self):
        print('finance')

h = HR()
h.name()
i = IT()
i.name()
d = Design()
d.name()
q = QA()
q.name()
f = Finance()
f.name()


#--------------------------------------------------------------------------------
class Car(ABC):
    @abstractmethod
    def name(self):
        pass
class Verna(Car):
    def name(self):
        print('Verna')
class SUV(Car):
    def name(self):
        print('SUV')
class Mustang(Car):
    def name(self):
        print('Mustang')
class Zen(Car):
    def name(self):
        print('Zen')
class Swift(Car):
    def name(self):
        print('Swift')
v = Verna()
v.name()
s = SUV()
s.name()
m = Mustang()
m.name()
z = Zen()
z.name()
sw = Swift()
sw.name()

#---------------------------------------------------------------------------
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print('bow')
class Cat(Animal):
    def sound(self):
        print('meow')
class Cow(Animal):
    def sound(self):
        print('moo')
d = Dog()
d.sound()
c = Cat()
c.sound()
co = Cow()
co.sound()
#----------------------------------------------------------------

# public and protected and private variables

class Simple:
    def __init__(self, a, b, c):
        self.a = a           
        self._b = b          
        self.__c = c        
    def m1(self):
        return self.a
    def m2(self):
        return self._b
    def m3(self):
        return self.__c


o = Simple(1,2,3)
print(o.a)  
print(o._b)  
o.m1()   
o.m2()  

#-----------------------------------------------------------
class Employee:
    def __init__(self,name,id,salary):
        self.name = name           
        self._id = id              
        self.__salary = salary     
    def Name(self):
        print(self.name)        
    def id(self):
        print(self._id)           
    def salary(self):
        print(self.__salary)    
e= Employee("Adarsh",169,30000)
print(e.name)     
print(e._id)      
e.Name()  
e.id()  
e.salary()
