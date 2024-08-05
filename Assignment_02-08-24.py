"""
1.Write a program which will find all such numbers which are divisible by 7 but are not a 
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
printed in a comma-separated sequence on a single line.
"""
for i in range(2000,32001):
    if i%7==0 and i%5!=0:
        print(i,end=',')
    

"""
2.With a given integral number n, write a program to generate a dictionary that contains (i, 
i*i) such that is an integral number between 1 and n (both included). and then the program 
should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
dic = {}
n = input("Enter a number :")
if n.isdigit():
    for i in range(int(n)+1):
        key = i
        value = i*i
        dic[key]=value
else:
    print("Enter proper Number")
print(dic)

"""
3.Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. Suppose the following input 
is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
'33', '12', '98'] ('34', '67', '55', '33', '12', '98')

"""
a = input("Enter the elements here with comma seperated :")
b = a.split(',')
c= tuple(b)
print(b,end='')
print(c)


"""
4.Write a program that accepts a comma separated sequence of words as input and prints 
the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
following input is supplied to the program: without, hello, bag, world Then, the output 
should be: bag,hello,without,world
"""
a = input("Enter the words here with comma seperated :")
b = a.split(',')
print(b)
b.sort()
print(b)
#or
d = a.split(',')
c = sorted(d)
print(c)

"""
5.Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3
"""
e = input('Enter the elements :')
l = 0
d = 0
sp = 0
for i in e :
    if i.isalpha():
        l = l + 1
    elif i.isdigit():
        d = d + 1
    else:
        sp = sp + 1
print('Letters :',l)
print('Digits :',d)
print('Special :',sp)

"""
6.Write a program that accepts a sentence and calculate the number of upper case letters 
and lower case letters. Suppose the following input is supplied to the program: Hello 
world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

"""
st = input("Enter the string here :")
up = 0
lo = 0
sp = 0
for i in st :
    if i.islower():
        lo = lo + 1
    elif i.isupper():
        up = up + 1
    else:
        sp = sp + 1
print("The Uppercase Letters :",up)
print("The Lower case letters :",lo)
print("The Special casse letters :",sp)


"""
7.Write a program that computes the net amount of a bank account based a transaction 
log from console input.The transaction log format is shown as following: D 100 W 200 D 
means deposit while W means withdrawal. Suppose the following input is supplied to the
program: D 300 D 300 W 200 D 100 Then, the output should be: 500 
""" 

bal = 0
type = ''
mon = ''
dep_wdr = input("Enter deposit or withdrawal : ")
li = dep_wdr.split()
print(li)
l = len(li)
if li!='' and li[0]=='W' or li[0]=='D':
    for i in range(0,l,2):
        type =li[i]
        mon = li[i + 1]
        if type == 'D':
            bal = bal +int(mon)
        if type == 'W':
            bal= bal-int(mon)
print(bal)


"""
8.A website requires the users to input username and password to register. Write a 
program to check the validity of password input by users. Following are the criteria for 
checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 Your program should accept a sequence of 
comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma. Example 
If the following passwords are given as input to the program: ABd1234@1,a 
F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

"""
sm = 'abcdefghijklmnopqrstuvwxyz'
ca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
di = '123456789'
sy = '$#@'
mi = 6
mx = 12
passwords = input("Enter your Passwords :")
pa2 = passwords.split(',')
for password in pa2:
    password = password.strip()  
    if len(password)<=12 and len(password)>=6 and (b in sm for b in password) and (c in ca for c in password) and (d in di for d in password) and  (e in sy for e in password):
        print(password)


"""
Define a function which can print a dictionary where the keys are numbers between 1 
and 20 (both included) and the values are square of keys
"""
dic = {}
def square():
    for i in range(1,11):
        key = i
        value = i*i
        dic[key]=value
    print(dic)
square()

"""
10.Define a function which can generate a list where the values are square of numbers 
between 1 and 20 (both included). Then the function needs to print the last 5 elements in 
the list
"""

def sq():
    li = []
    for i in range(1,21):
        sq = i*i
        li.append(sq)
    l = len(li)
    last = li[l:l-6:-1]
    print(last)
sq()




