# public attributes and method

class Encap:
    def __init__(self,value):
        self.value = value
    def m1(self):
        print(self.value)
e = Encap(100)
print(e.value)
e.m1()
    
# protected attributes and method

class Encap1:
    def __init__(self,value):
        self._value = value
    def m1(self):
        print(self._value)
e = Encap1(1600)
print(e._value)
e.m1()

# private attributes and method

class Encap2:
    def __init__(self, value):
        self.__value = value

    def m1(self):
        print(self.__value)
e = Encap2(99)
#print(e.__value) # not accesseble outside of the class
e.m1()


#------------------------------------------------------------------------
class Pub:
    def __init__(self,x):
        self.x = x
    def m1(self):
        print(self.x)

class Prot:
    def __init__(self,y):
        self._y = y
    def m1(self):
        print(self._y)

class Priv:
    def __init__(self,z):
        self.__z = z
    def m1(self):
        print(self.__z)

p = Pub(100)
p.m1()
print(p.x)

q = Prot(789)
q.m1()  
print(q._y)

r = Priv(987)
r.m1()  
#print(r.__z)
#---------------------------------------
class Pub:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def m1(self):
        print(self.name,self.id)

class Prot:
    def __init__(self,company,salary): 
        self.company = company
        self.salary = salary
    def m1(self):
        print(self.company,self.salary)

class Priv:
    def __init__(self,phone,pricee): 
        self.phone = phone
        self.pricee = pricee
    def m1(self):
        print(self.phone,self.pricee)

p = Pub('Adarsh',169)
p.m1()

q = Prot('Wipro',100000)
q.m1()  


r = Priv('Mi Note 10 S',18000)
r.m1()  
#print(r.__z)
