# line -53  removing repeated characters from string----------------------------------------------------------------
a ='removing repeated characters from string'
new = ''
for i in a:
    if i not in new:
        new = new+i
print(new)


# line 54 Python program to check given character is vowel or consonant.--------------------------------------------
char = input("Enter a Single Character :")
b = len(char)
vowels = "aeiouAEIOU"
if b ==1 and char.isalpha():
    if char in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid Character")



# line 55 Python program to check given character is digit or not.--------------------------
# for single digit

dig = input("Enter a digit :")
ln = len(dig)
if ln ==1:
    if dig.isdigit():
        print("The Given input is Digit")
    elif dig.isalpha():
        print("Alphabet")
    else:
        print("Special Character")
else:
    print("Invalid input")


# for multiple characters
inpu = input ("Enter a something :")
if inpu.isalnum():
    if inpu.isalpha():
        print("Input is Alphabets")
    elif inpu.isdigit():
        print("Input is Digits")
    else:
        print("Input is Alpha Numeric ")
else:
    print("Input is Special Character")


#line 56 Python program to delete vowels in a given string.-------------------------------------------------------------
a = "Python program to delete vowels in a given string."
vow = "aeiouAEIOU"
new = ''
for i in a:
    if i in vow:
        pass
    else:
        new = new+i
print(new)


# line 60 Python program to count alphabets, digits and special characters.-----------------------------------------
a = "Python2 267program%^& to delete 38022901vowels in 2912910a given %#$^^)string."
dig = 0
alph = 0
special = 0
for i in a:
    if i.isalpha():
        dig= dig + 1
    elif i.isdigit():
        alph = alph +1
    else:
        special = special +1   
print(dig)
print(alph)
print(special)


# line 61 Python program to check given character is digit or not using isdigit() method.------------------------
a = input("Enter a single digit :")
numbers = '123456789'
alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym = '!~#$%^&*'
ln = len(a)
if ln == 1:
    if a in numbers:
        print("Given input is digit")
    elif a in alph :
        print("The Gven Input is Alphabets")
    elif a in sym :
        print("The given input is symbol")
    else:
        print("Other Character")
else:
    print("Enter only a character")


# line 62 Python program to calculate sum of integers in string.-------------------------------------
string = "Python 10 20 program20 to67 calc233ulate7269 sum o32323f inte33gers323 in string."
sum = 0
for i in string:
    if i.isdigit():
        sum = sum +int(i)
print(sum)


# using list
string = "Python 10 20 program20 to67 calc233ulate7269 sum o32323f inte33gers323 in string."
list1= []
sum = 0
for i in string:
    if i.isdigit():
        list1.append(int(i))
for a in list1:
    sum = sum + a
print(sum)
print(list1)



# line 63 Python program to print all non repeating character in string.
string = 'aabbc'
new = ''
for i in string:
    count = string.count(i)
    if count ==1 and i not in new :
        new = new + i
print(new)


# line 54 Python program to check given character is vowel or consonant..-----------------------------------
char = input("Enter a characters :")
ln = len(char)
vowels = "aeiouAEIOU"
if ln ==1:
    if char in vowels:
        print("It is vowel")
    else:
        print("Consonant")
else:
    print("enter A single Character")



#line 64 Python program to copy one string to another string.
org = 'Python program to copy one string to another string.'
copy = ''
for i in org :
    copy = copy + i
print(copy)



# line 57 Python program to count the Occurrence Of Vowels & Consonants in a String.
string = 'Python program to count the Occurrence Of Vowels & Consonants in a String.'
vowcount = 0
vowels = "aeiouAEIOU"
consocount = 0
for i in string:
    if i in vowels:
        vowcount= vowcount+1
    else:
        consocount= consocount+1
print("The Number Of Vowels In the String :",vowcount)
print("The Number Of Consonent In the String :",consocount)


