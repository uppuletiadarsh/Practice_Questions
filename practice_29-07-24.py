
# How do you create a empty tuple on python ?
# m -1
t = tuple()
print(t)
print(type(t))


# Write a python program to unpack atuple into several variables ?
c,b,d=(10,20,30)
print(c)
print(b)
print(d)

# Write a python proram to convert tuple into a string ?
t1 = (1,3,3,5,6,)
new = ''
for i in t1:
    new = new + str(i)
print(new)
print(type(new))

# Write a python program to find most frequent element in tuple ?
b = (1,2,3,2)
new = []
for i in b :
    count= b.count(i)
    new.append(count)
m = max(new)
i = new.index(m)
res = b[i]
print('the frequent number is :',res)

# write a python program to add an item to the tuple ? 
# m -1
t = (1,2,3,4)
l = list(t)
l.append('python')
l.append('java')
new = tuple(l)
print(new)
print(type(new))

# m - 2
t = (1,2,3,4)
new = t + ('python','Adarsh')
print(new)

# m - 3
t1 = (1,2,3,4)
t2 = 'python','.net','testing'
t3 = True,False,10.90
new = t1+t2+t3
print(new)

