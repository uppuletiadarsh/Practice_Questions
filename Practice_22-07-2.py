# line - 68 Python program to insert an element at end of an Array.
arr = [1,2,34,5]
arr.append(1000)
print(arr)

# ex
new = []
for i in range(10,20):
    new.append(i)
print(new)
# ex
alp = []
for i in range(65,123):
    letter = chr(i)
    alp.append(letter)
print(alp)


# line 79 Python program to insert element at a given location in Array.
arr = [1,2,3,4444,5,6,78,8]
arr.insert(3,"Adarsh")
print(arr)
arr = [1,2,3,4,5,6,7,8,9]
print("The list :",arr)
ln = len(arr)-1
print("The maximum Position :",ln)
ins = int(input("Enter a position :"))
char = eval(input("Enter element :"))
if ins < ln and ins > 0:
    arr.insert(ins,char)
else:
    print("enter The Proper Position")
print(arr)


# line 80 Write a python program  to check teh sizes of givrn two list are same.
list1 = eval(input("Enter List1 :"))
list2 = eval(input("Enter List2 :"))
if len(list1)==len(list2):
     print("Size Of both list are same")
else:
     print("size of both lists are Not same")



# line - 81 Python program to create a list. (all posible ways)
# m -1
lst = eval(input("Enter list enclosed in square braces :"))
print(type(lst))
print(lst)

# m -2 
lst = [1,2,3,3.6,"Adarsh",True]
print(lst)

# m - 3
ele = input("Enter the values with Comma seperated :")
lst = ele.split(',')
print(lst)

# m -4 
stri = input("enter any string :")
lst = list(stri)
print(lst)



# line - 82 Python program to access a given element from the nested list ? 
lst = [1,2,3,[4,5,6,[8,9,10],100,200],900,"Adarsh"]
print(lst)
ele = 9
print(lst[3][3][1])


 
# line - 83 Write a python program to find largest and smallest  number in an list.
# m - 1
lst = [100,50,200,400]
maxi = lst[0]
mini = lst[0]
for i in lst :
    if maxi < i :
        maxi = i
    elif i < mini:
        mini = i
print("The Max num is :",maxi)
print("The Min num is :",mini)

# m- 2
lst = [100,50,200,400]
maximum = max(lst)
minimum = min(lst)
print(maximum)
print(minimum)

# m- 3
lst = [100,50,200,400]
b = sorted(lst)
print("The max is :",b[-1])
print("The mini is :",b[0])


# line - 84 Write a python program  to find  sum of list elements ?
# m -1
lst = [100,50,200,400] 
sum = 0
for i in lst:
        sum = sum + i
print('The sum is :',sum)

# m -2
lst = [100,50,200,400]
sum = 0
c = 0
ln = len(lst)
while c < ln :
     sum = sum + lst[c]
     c = c + 1   
print(sum) 


# line - 85  Python program to find heighest frequency elemnt in list
lst = [100,50,200,400,50,100,50]
new = []
for i in lst :
     count = lst.count(i)
     new.append(count)
maxi = max(new)
ind = new.index(maxi)
hf = lst[ind]
print("The High Frequency number is :",hf)
          
     
#  line - 86  Python program to reverse an list in two ways ?
lst = [100,50,200,400,50,100,50]
# slicing
rev1 = lst[::-1]
print(rev1)

# for loop
new = []
for i in range(len(lst)-1,-1,-1):
    new.append(lst[i])
print(new)



    



