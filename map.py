# Python Collections Library 

# List :- is a collection which is ordered and changeable.Allow duplicate values.

# Tuple :- is a collection which is ordered and unchangeable.Allow duplicate values.

# Set :- is a collection which is unordered and unchangeable(but you can remove or add items),
#        and unindexed.No duplicate values.

# Dictionary :- is a collection which is ordered and changeable.No duplicate values.


# Map function :-

# Syntax :- map(function,iterables);
# Map function returns a map object.

# 1

print ('Map with  function')

def multiply(i):
    return i*i

x=map(multiply,(3,4,5,6,7))

print(list(x))

# 2

print("Map with tuple")

def upper(a):
    return a.upper()

y=map(upper,('this','is','map'))

print(tuple(y))

# 3

print("Map with built in function")

z=map(len,["welcome","to","sem3"])

print(list(z))

# 4

print("Map with lambda")

a=map(lambda x:x+x,(6,7,8,9))

print(list(a))

# 5

print("Map with dictionary")

car_dict={'a':'Mercedes-Benz','b':'BMW','c':'Ferrari','d':'Lamborghini','e':'Jeep'}

car_dict = dict(map(lambda x:(x[0],x[1]+'_'),car_dict.items()))

print(car_dict)

# 6

print("Map with set")

def example(i):
    return i%3

exm ={33,102,62,96,44,28,227}

upd = map(example,exm)

print(set(upd))

print("\n--------------Assignment------------\n")

# Assignment 


# 1

print("\n1. Triple all the numbers given in list.\n")

def triple(a):
    return a+a+a

tri=(2,3,4,5)

print("Original list : ", tri)

ans=map(triple,tri)

print("Triple of list : ",list(ans))

# 2

print("\n2. Separate even odd numbers from given list (range(0,10)).\n")
    
# map returns true or false and so to filter out that we use filter function.

lst=(0,1,2,3,4,5,6,7,8,9)
print("list : ", lst)

even=filter(lambda x: x %2==0,lst)
print("\neven : ",list(even))

odd=filter(lambda x: x %2!=0,lst)
print("odd  : ",list(odd))

# 3

print ("\n3. print all string in lower case from given tuple.\n")

def fun_low(i):
    return i.lower()

tup_exm =("THIS","IS","TUPLE")
print("Original Tuple : ",tup_exm)

show=map(fun_low,tup_exm)

print("Lower Case : ",tuple(show))

# 4

from ast import Return
import math

print ("\n4. print Square root of numbers given in list.\n")

num = (4,9,16,25,40)
print("Original list : ",num)

sqrt_exm =map(math.sqrt,num)

print("Square root of numbers : ",list(sqrt_exm))

# 5

from collections import OrderedDict

print ("\n5. Eliminate duplicate letters from given string.\n")

def rm_duplicate(i):
    return "".join(OrderedDict.fromkeys(i))

str = ("helloworld","mississippi","aryan")
print("Original string : ",str)

upd=map(rm_duplicate,str)

print("Removing duplicate letters : ",list(upd))

# 6

print("\n6. Print table of any number.\n")

# Taking input 

# i =int(input("Enter a number: "))

i=(2)
print("number : ",i)

def fun(x):
    return x*i

lst=(1,2,3,4,5,6,7,8,9,10)
res =list(map(fun,lst))

print("Multiplication Table : ",res)

#Normal way to print a multiplication table.

# num=int(input("Enter a number : "))

# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

# 7

print("\n7. Add two list\n")

def add(x,y):
    return x + y

lst1 =(1,2,3,4,5,"ab")
print("List 1 : ",lst1)

lst2 =(6,7,8,9,10,"cd")
print("List 2 : ",lst2)

result = map(add,lst1,lst2)

print("\nAddition of two : ",list(result))

# 8

print("\n8. Convert all float digits into integer.\n")

lst = (2.45,5.78,9.6,7.800,8.0,4)
print("Original list : ",lst)

rslt=list(map(int,lst))

print("Float To Integer : ",rslt)

# 9 (incomplete or unsolved)

print ("\n9. Reverse given list.\n")

def rev(i):
    return reversed(i)

lst = ('1','2','3','4','5')
print("Original list : ",lst)

reverse = list(filter(rev,('1','2','3','4','5')))

print("reverse :",reverse)

# 10

print ("\n10. Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.\n") 

gmail = {'a':'aryan03','b':'vinay06','c':'rex23','d':'divya23'}
print("Original dictionary : ",gmail)

gmail = dict(map(lambda x:(x[0],x[1]+'@gmail.com'),gmail.items()))

print("Gmail :",gmail)

# ---------------------------------------------------------------------------------------------------- #

# Filter Function
print("\nFilter Function.\n")
# Syntax :- filter(function,iterables)

# map creates a new array by transforming every element in an array individually.
# filter creates a new array by removing elements that don't belong.

# Example :-

# 1

print("\nExample : Filter for even number.\n")

# i=(range(1,11))
i=[1,2,3,4,5,6,7,8,9,10]
print("Original list : ",i)

def even(i):
    if i % 2 == 0:
        return True
    return False

check = list(filter(even,i))

print("Even Numbers : ",check)

# 2

print("\nExample : Checking Vowels using Filter.\n")

letters = ['a','b','c','d','e','f']
print("Original Tuple : ",letters)

def vowel(letters):
    vowels=['a','e','i','o','u']
    return True if letters in vowels else False

check_vowel = tuple(filter(vowel,letters))

print("Vowels : ",check_vowel)

# 3

print("\nExample : Filter with Lambda.\n")

num=[1,2,3,4,5,6,7,8]
print("Original List : ",num)

Even = list(filter(lambda x:(x%2==0),num))

print("Even Numbers : ",Even)

print("\n--------------Assignment------------\n")

# Assignment 


# 1

print("\n1. Using filter() function filter the list so that only negative numbers are left.\n")

Num =(-3,-2,-1,0,1,2,3)
print("Original List : ",Num)

def Neg(Num):
    if Num<0:
        return True
    return False

check_neg = list(filter(Neg,Num))
# (Or) check_neg = list(filter(lambda x:x<0,Num))

print("Negative Numbers : ",check_neg)

# 2

print("\n2. Using filter function,filter the even numbers so that only odd numbers are passed to the new list.\n")

lst = (1,2,3,4,5,6,7,8)
print("Original list : ",lst)

def odd(lst):
    if lst%2!=0:
        return True
    return False

check_odd = list(filter(odd,lst))
print("Odd Numbers : ",check_odd)

# 3 

print("\n3. Using filter() and list() functions and .lower() method filter all the vowels in a given string.\n")

str1=('a','B','E','c','z')
print("Original List : ",str1)

lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))
print("Vowels : ",lst)

# 4

print("\n4. Using filter() and list() functions filter all the positive integers in the string.\n")

lst = (-3,-2,-1,0,1,2,3)
print("Original list : ",lst)

positive = list(filter(lambda x:x>=0,lst))
print("Positive Number : ",positive)

# 5 

print("\n5. Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.\n")

# here, first we use map to change signs and then select positive numbers using filter.
exchange = (-65,-27,-15,30,19,63)
print("Original list : ",exchange)

change = list(filter(lambda x:True if x>0 else False,map(lambda x:x*(-1),exchange)))
print("After change : ",change)

# 6

print("\n6. Using map() and filter() functions add 3500 to the values below 9000.\n")

salary = {'a':10000,'b':9500,'c':5000,'d':6000,'e':2000}
print("Original Salary : ",salary)

added = dict(map(lambda x:(x[0],x[1]+3500),filter(lambda x:(x[1]<9000),salary.items())))
print("Added Salary : ",added)
