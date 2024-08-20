# inheritance

class A :
    def __init__(self):
        self.name = 'Avinesh'
    def m1(self):
        print(self.name)
class B(A):
    def m2(self):
        print(self.name)

c = B()
c.m2()

# single inheritance

class Car :
    def __init__(self):
        self.wheels = 4
    def m1(self):
        print(self.wheels)
class Drive(Car):
    def m2(self):
      print('The car contains ',self.wheels)
c = Drive()
c.m2()

class Grandfather:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print('this is Grandfather')
class Father(Grandfather):
    def __init__(self, name, occupation):
        Grandfather.__init__(self, name)
        self.occupation = occupation
    def work(self):
        print(self.name)
        print("Father is working and the Occupation is ",self.occupation)
c = Father("adarsh", "developer")
c.speak()
c.work()


# multiple inheritance

class Father:
    def m1(self):
        print('hello from Father')
    def m2(self):
        print('father is working')
class Mother:
    def m3(self):
        print('mother is cooking')
    def m4(self):
        print("mother is cleaning")
class Child(Father, Mother):
    def m5(self):
        print("child is playing")
c= Child()
c.m1()
c.m2()
c.m3()
c.m4()
c.m5()

class Car:
    def wheels(self):
        print(4)
class Bike:
    def tires(self):
        print(2)
class Vehicle(Car, Bike):
    def start(self):
        print("Vehicle is starting")
v = Vehicle()
v.wheels()
v.tires()

# multilevel inheritance

class G:
    def method1(self):
        print("method in G")
class F(G):
    def method2(self):
        print("method in F")
class C(F):
    def method3(self):
        print("method in C")
c = C()
c.method1()
c.method2()
c.method3()

class A:
    def method1(self):
        print("method 1 in A")
    def method2(self):
        print("method 2 in A")
class B(A):
    def method3(self):
        print("method 1 in B")
    def method4(self):
        print("method 2 in B")
class C(B):
    def method5(self):
        print("method 1 in C")
    def method6(self):
        print("method 2 in C")
class D(C):
    def method7(self):
        print("method 1 in D")
    def method8(self):
        print("method 2 in D")
c = D()
c.method1()
c.method2()
c.method3()
c.method4()
c.method5()
c.method6()
c.method7()
c.method8()

# Hierarchical inheritance

class A:
    def method1(self):
        print("method 1 in A")
    def method2(self):
        print("method 2 in A")
class B(A):
    def method3(self):
        print("method 1 in B")
    def method4(self):
        print("method 2 in B")
class C(A):
    def method5(self):
        print("method 1 in C")
    def method6(self):
        print("method 2 in C")
b = B()
c = C()
b.method1()
b.method2()
b.method3()
b.method4()
c.method1()
c.method2()
c.method5()
c.method6()

class Father:
    def m1(self):
        print("Father from m1")

    def m2(self):
        print("father from m2")

class Son(Father):
    def m3(self):
        print("Son from m3")

    def m4(self):
        print("Son from m4")

class Daughter(Father):
    def m5(self):
        print("Daughter from m5")

    def m6(self):
        print("Daughter from m6")
s = Son()
d = Daughter()

s.m1()
s.m2()
s.m3()
s.m4()
d.m1()
d.m2()
d.m5()
d.m6()

# hybrid inheritance
class A:
    def method1(self):
        print("from class a")
class B(A):
    def method2(self):
        print("from class b")
class C(A):
    def method3(self):
        print("from class c")
class D(B, C):
    def method4(self):
        print("from class d")
d = D()
d.method1()
d.method2()
d.method3()
d.method4()

class A:
    def method1(self,x):
        print('from class A with value',x)
class B(A):
    def method2(self,y):
        print('from class B with value',y)
class C(A):
    def method3(self, x, y):
        print('from class C with values',x,'and', y)
class D(B, C):
    def method4(self, x, y):
        print("from class D with values", x,"and",y)
d = D()
d.method1(10)
d.method2(20)
d.method3(30, 40)
d.method4(50, 60)

class A:
    def method1(self, name):
        print('from class A with name',name)
class B(A):
    def method2(self, name):
        print('from class B with name',name)
class C(A):
    def method3(self, name1, name2):
        print('from class C with names',name1,'and',name2)
class D(B, C):
    def method4(self, name1, name2):
        print('from class D with names',name1,'and',name2)
d = D()
d.method1('Adarsh')
d.method2('Avinesh')
d.method3('Adhya', 'Abhi')
d.method4('Siddu', 'Navdeep')


     
