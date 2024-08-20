# super()
class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def details(self):
        print(self.name)
        print(self.id)
class Child(Parent):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    def details(self):
        print(self.name)  
        print(self.id)
        print(self.salary)

c = Child('Adarsh', 169, 100000)
c.details()
#---------------------------------------------------------------------
class Car:
    def __init__(self,company,year,colour):
        self.company = company
        self.year= year
        self.colour= colour
    def details(self):
        print(self.company)
        print(self.year)
        print(self.colour)
class Vehicle(Parent):
    def __init__(self,company,year,colour):
        super().__init__(company,year,colour)
    def details(self):
        super().details()
c = Child('Maruthi',2022,'red')
c.details()
#-----------------------------------------------------------------
class P:
    b = 20
    def __init__(self):
        self.a = 20
class C(P):
    def m1(self):
        print(self.a)
        print(super().b)
c = C()
c.m1()

#-----------------------------------------------------
class P:
    def __init__(self):
        print('This is Constructor ')
    def m1(self):
        print('This is instance Method')
    @classmethod
    def m2(cls):
        print('this is Class Method')
    @staticmethod
    def m3():
        print('This is Staticmethod')
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
    def m4(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c = C()
c.m4()
#-------------------------------------
class P:
    def __init__(self):
        print('This is Constructor ')
    def m1(self):
        print('This is instance Method')
class C(P):
    @classmethod
    def m2(cls):
        super(P,cls).__init__(cls)
       
c = C()
c.m2()
#----------------------------------------------
class P:
    def __init__(self):
        print('This is Constructor ')
    def m1(self):
        print('This is instance Method')
    @classmethod
    def m2(cls):
        print('this is Class Method')
    @staticmethod
    def m3():
        print('This is Staticmethod')
class C(P):
    @staticmethod
    def m1():
        super(P,P.m3())
c = C()
c.m1()