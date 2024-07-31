
# Write a python program to  add a key to a dictionary ?
# m -1
d = {'comany':"skywaves",'locality':'Kondapur'}
d['name']='Adarsh'
d['age']='24'
d['role']='Python developer'
print(d)

# m - 2
d = {'comany':"skywaves",'locality':'Kondapur'}
d1 ={'name':'Adarsh'}
d.update(d1)
print(d)

# Write a python program to check weather the given value is present in the dictionary or not ?

i = eval(input("enter the value :"))
dic = {'one':1,'two':2,'name':"adarsh",'age':24,'key':'Value'}
key = dic.values()
if i in key:
    print("Yes exist")
else:
    print("Not exist")

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"
dic = {}
for i in range(1,16):
    key = i
    value = i*i
    dic[key]=value
print(dic)

## Write a python program to create a dictionary from the string ?

st = 'Ad1%'
key = ''
value = ''
dic ={}
for i in st :
    if i.islower():
        key = i
        value="it is lower "
        dic[key]=value
    elif i.isdigit():
        key = i
        value="it is digi "
        dic[key]=value
    elif i.isupper():
        key = i
        value="it is Upper "
        dic[key]=value
    else:
        key = i
        value="it is Special Char "
        dic[key]=value
print(dic)

# Write a python program to merge two python dictionaries ?
d1 = {'name':'adarsh','role':'python developer'}
d2 = {'age':24,'company':'skywaves'}
d1.update(d2)
print(d1)

# Write  a python program to sort dictionary by keys or values ?
#m -1
a = {'b':10,'a':20,'d':30,'c':40}
new = {}
re = sorted(a.items())
print(re)

#m - 2
bc = sorted(a.keys())
for i in bc :
    key = i
    value = a[i]
    new[key]=value
print(new)

# m - 3
cd = sorted(a.values())
print(cd)

#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"

st = input("Enter a string :")
count = 0
di = {}
if st.isalpha:
    for i in st :
        count = st.count(i)
        di[i]=count
else:
    print("Enter only alphabets")
print(di)


# Write a python program to combine two dictionaries by adding values of common keys ?

d1 = {'a':100,'b':200,'c':300,'d':400}
d2 = {'c':1000,'d':2000}
new = {}
key1 = d1.keys()
key2 = d2.keys()
for i in key1:
    if i in key2:
        sum = d1[i]+d2[i]
        new[i]=sum
print(new)


