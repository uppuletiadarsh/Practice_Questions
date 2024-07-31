"""
Write a python program to collect data from a user and store it in a dictionary, 
you can use Python's built-in functions like input() to get user input and then organize that input into a dictionary. 
Note :- Data is employee name, domain, performance(like credits = 3/5).
"""
# The Employee data in dictionary
print("Enter The employee Data here Below")
num = int(input("Enter The Number Of employees :"))
dic = {}
for i in range(num):
    name = input("Enter the Employee name :")
    Domain = input('Enter the Domain :')
    Performance = int(input("Enter The credits for employee out of 5 :"))
    if name!='' and Domain!='' and Performance < 5 :
        dic['Name']=name
        dic['Domain']=Domain
        dic['Credits Out of 5']=Performance
    else:
        print("Enter Proper data")
print(dic)


## packing and Unpacking of tuple
a = (10,20,30)
b,c,d = a
print(b)
print(c)
print(d)

dta = ("Adarsh",24,"Python Developer")
name,age,role=dta
print(name)
print(age)
print(role)

# dictionary from user
ele = input("Enter the number of elements  :")
dic = {}
if ele.isdigit():
    for i in range(int(ele)):
        key = input("Enter the key :")
        value = input("Enter The Value :")
        dic[key]=value
print(dic)
        
