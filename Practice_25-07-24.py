# line - 103 Write a program to create a set.
# m - 1
set1 = {1,"Adarsh",False,10.90}
print(set1)

# m- 2
a = [1,3,44,5,6,64,2,434,85,"Adarsh",True,False]
set2 = set(a)
print(set2)

# m - 3
b = (1,"adarsh",False,10.56)
set3 = set(b)
print(set3)

# m - 4
set4 = set()
ele = int(input("enter the no. elements in set :"))
if type(ele)==int:
    for i in range(ele):
        name = input("Enter the element :")
        set4.add(name)
else:
    print("Enter the proper number")
print(set4)


# line - 104 Write program to iterate over sets.
set5 = {1,2,3,4,5,6,7,8}
for ele in set5:
    print(ele,end=' ')



# line - 105 Write a Python program to add member to a set.
# m - 1
set6 = {1,2,3,4,5,6,7,8}
set6.add(100)
print(set6)

# m - 2
for i in range(100,115):
    set6.add(i)
print(set6)


# line - 106 Write a Python program to remove item from a given set.
set7 = {1,2,3,4,5,6,7,8}
set7.remove(5)
print(set7)


# removing even numbers
set7 = {1,2,3,4,5,6,7,8}
set8 = set7.copy()
for i in set8:
    if i % 2 == 0:
        set7.remove(i)
print(set7)



# line 107 Write a python program to create a intersection of set ?
facebook_users = {"Aadarsh","Avinesh","Siddarth","Anvesh","Vamshi"}
insta_users = {"Aadarsh","teja","Abhi","Sunny","Ram","Avinesh"}
twitter_users = {"Abhi","Aadarsh","teja","Chinna"}
res = facebook_users.intersection(insta_users,twitter_users)
print(res)



# line 108 Write a python program to createa unionof set ?
google_india = {'hyderabad','delhi','Kolkata',"banglore"}
google_other_cities = {'newyork','France','Shanghai','london','mascow','Rome'}
all_google_branches = google_india.union(google_other_cities)
print(all_google_branches)



# line  109 Write a python program to create set differance ? 
python_team = {"task 1", "task 2", "task 3"}
java_team = {"task 2", "task 3", "task 4"}
task_completed_by_python_team = python_team.difference(java_team)
print("tasks completed by Python Team only:", task_completed_by_python_team)



# line 110 Write a python program to create a symmetric defferance ?
netflix = {'action','thriller','anime','family entertainers'}
disney = {'horror','action','family entertainers'}
non_common = netflix.symmetric_difference(disney)
print(non_common)



# line 111 write a python program to find max and min values in a set?
the_set = [10,20,30,44,50,60]
maxi = max(the_set)
mini = min(the_set)
print(maxi)
print(mini)



# line 112 Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
set1 = {1,2,3,4}
s = set1.copy()
set2 = {3,4,5,6}
new = set()
for i in s:
    if i not in set2:
        new.add(i)
print(new)



# line 113 Write a Python program to remove items 10, 20, 30 from the following set at once.?
s = {10,20,30,40,50,60}
s1 = s.copy()
ele = 10,20,30
for i in s1 :
    if  i in ele:
        s.remove(i)
print(s)



# line 114 Check if two sets have any elements in common. If yes, display the common elements?
s1 = {1,2,3,4,5,6}
s2 = {7,8,9,10}
count = 0
for i in s1:
    if i in s2:
        count = count+1
if count > 0:
    print("Yes Contains Common element")
else:
    print("No Common Elements")



# line 115 Update set1 by adding items from set2, except common items?
s1 = {1,2,3,4,5,6}
s2 = {7,8,9,10}
for i in s2:
    if i not in s1:
        s1.add(i)
print(s1)



# line 116 Remove items from set1 that are not common to both set1 and set2?
s1 = {1,2,3,4,5,6}
s = s1.copy()
s2 = {6,5,7,8,9,10}
for i in s:
    if i not in s2 :
        s1.remove(i)
print(s1)