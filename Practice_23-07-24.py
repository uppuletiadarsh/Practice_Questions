# line - 88 Write a python program to merge two list? 
# m - 1
l1 = [1,2,3,4,5]
l2 = [100,200,300]
l1.extend(l2)
print(l1)

# m - 2
l1 = [1,2,3,4,5]
l2 = [100,200,300]
merge = l1 + l2
print(merge)

# m - 3
l1 = [1,2,3,4,5]
l2 = [100,200,300]
merge = []
for i in l1:
    merge.append(i)
for b in l2:
    merge.append(b)
print(merge)
# m - 4
l1 = [1,2,3,4,5]
l2 = [100,200,300]
merge = l1[:] + l2[:]
print(merge)


# line - 89 Write a python program to delete element of given index in list ?

list1 = [100,200,300,400,500,600,700]
ln = len(list1)-1
print("the max index number is :",ln)
ind = int(input("Enter the index :"))
print(list1.pop(ind))
    

# line - 90 Write a pytho program to delete given element from the list?

list1 = ["Adarsh",100,200,True,False,100.70]
print("The List is :",list1)
ele = eval(input("Enter the ele :"))
if ele in list1:
    list1.remove(ele)
    print(list1)
else:
    print("Enter a Proper element")


# line - 91 Write a python programe to check if the two list are having atleast one common element?
list1 = [1,2,3,4,5,6]
list2 = [20,30,40,70,5]
new = []
for i in list1 :
    if i in list2:
       new.append(i)
if len(new) > 0 :
    print('Yes the lists are contain common element')
else:
    print('No common elements')


# line - 92 Write a python program to remove  specified column from the nestedlist?

li = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
ind = 1
for i in li:
    if ind < len(i):
        del i[ind]
for i in li:
    print(i)


# line - 93 Write python program to convert a list of integers into single integer ?

li = [1,2,3,4,5,6,7]
new = ''
for i in li :
    new =new + str(i)
print(int(new))

# line - 94 Write  a python programe to remove duplicates from the list ?
li = [1,1,2,2,3,3,4,5,4,5,6,6,7,7]
new = []
for i in li :
    if i not in new:
        new.append(i)
print(new)