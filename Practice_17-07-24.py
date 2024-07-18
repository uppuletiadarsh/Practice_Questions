# line -34 How do you find a length of a string ? ------------------------------------------------------------
#len()
string1 = input("Enter a string :")
length = len(string1)
print("The Length of the string :",length)


#line - 35 Write a program to calculate the sum of first 10 natural numbers ?------------------------------------
num = int(input("Enter a number :"))
sum = 0
for a in range(0,num+1):
    sum = sum+a
print(sum)


#line 36 Write a program to read integer and convert it into float ?----------------------------------------------
int_num = int(input("Enter a Integer :"))
print(int_num," :" ,type(int_num))
flt_num = float(int_num)
print(flt_num," :",type(flt_num))


#line 37 write a program to find grater among two numbers, take input from the key board ? -------------------------
num1 = eval(input("Enter a number 1 :"))
num2 = eval(input("Enter a number 2 :"))
if num1>num2:
    print("The",num1,"is Greater than ",num2)
elif num2==num1:
    print("Both are Equal")
else:
    print("The",num1,"is Lesser than ",num2)


# line 38 Take two inputs strings from the user, write python program to print gretest among them ? -------------
str1 = input("Enter a string 1 :")
str2 = input("Enter a string 2 :")
if str1>str2:
    print("The",str1,"is Greater than ",str2)
elif str1==str2:
    print("Both are Equal")
else:
    print("The",str1,"is Lesser than ",str2)


#line 39 write a program to find maximum of two numbers ? ----------------------------------------------
num1 = eval(input("Enter a number 1 :"))
num2 = eval(input("Enter a number 2 :"))
if num1>num2:
    print("The",num1,"is Greater than ",num2)
elif num2==num1:
    print("Both are Equal")
else:
    print("The",num1,"is Lesser than ",num2)

#another method ------max()
a = max(num1,num2)
print(a)


#line 40 Write a program to print given number is even or odd ? ------------------------------------------
number = int(input("Enter a number :"))
if number%2==0:
    print(number," : Is Even")
else:
    print(number," : Is Odd")


# line 41 Write a program to print given number is an positive or nagitive-----------------------------------

number = int(input("Enter a number :"))
if number < 0 :
    print(number," : Is Negative Number")
elif number==0:
    print(number," : Is Zero")
else:
    print(number," : Is Positive")


#line 42 Python Program to count occurrence of a given characters in string.--------------------------------
string = " Python Program to count occurrence of a given characters in string"
check = input("Enter a string That You want Check :")
res = string.count(check)
print(res)


#line 44 Python program to check a String is palindrome or not------------------------------------------
string = input("Enter a string to Check Palindrome :")
if (string[::-1]==string):
    print("The Given String Is Palindrome")
else:
    print("The Given String Is Not a Palindrome")


# line 45 Python program to replace the string space with a given character.-------------------------------
string = "Python program to replace the string space with a given character."
chr = input("Enter a string to Replace In the place Of Space :")
new = []
for i in string:
    if i == ' ':
        new.append(chr)
    else:
        new.append(i)
res = ''.join(new)
print(res)

#method -2
string = "Python program to replace the string space with a given character."
chr = input("Enter a string to Replace In the place Of Space :")
res = string.replace(' ',chr)
print(res)


#Python program to replace the string space with a given character using replace() method.--------------------
string = "Python program to replace the string space with a given character."
chr = input("Enter a string to Replace In the place Of Space :")
res = string.replace(' ',chr)
print(res)


#line 47 Python program to convert lowercase char to uppercase of string.--------------------------------
string = input("Enter the String That You Convvert Into Uppercase :")
res = string.upper()
print(res)


#line 48 Python program to convert lowercase vowel to uppercase in string.------------------------------
vow = "aeiou"
string = "Python program to convert lowercase vowel to uppercase in string."
new = ''
for i in string:
    if i in vow:
        new = new+i.upper()
    else:
        new = new+i
print(new)
        

#line 49 Python program to separate characters in a given string.---------------------------------------
string = "Python,program,to convert, lowercase vowel to uppercase in string."
sep = input("Enter the seperator comma or any char :")
res = string.split(sep)
print(res)



#line 50 Python program to remove blank space from string.----------------------------------------------
# for extra spaces
string = "  Python program to remove blank space from string   "
res = string.strip()
print(res)


#for removing spaces between words
string = "  Python program to remove blank space from string   "
new = ''
for i in string:
    if i !=' ':
        new = new+i
print(new)


#line 51 Python program to concatenate two strings using join() method.---------------------------------------
string1= input("Enter the String1 :")
string2= input("Enter the String2 :")
list1 =[string1,string2]
res = ' '.join(list1)
print(res)



#line 52 Python program to concatenate two strings without using join() method.---------------------------------
#method-1
string1= input("Enter the String1 :")
string2= input("Enter the String2 :")
res = string1+string2
print(res)


#method-2
string1= input("Enter the String1 :")
string2= input("Enter the String2 :")
res = ''
for i in string1:
    res = res+i
for b in string2:
    res=res+b
print(res)


# line 43 Python Program to check if two Strings are Anagram.-----------------------------------------------
string1= input("Enter the String1 :")
string2= input("Enter the String2 :")
a = string1.upper()
b = string2.upper()
c = a.replace(' ','')
d = b.replace(' ','')
e = sorted(c)
f = sorted(d)
if e == f  :
    print("Anagram")
else:
    print("Not a Anagram")










