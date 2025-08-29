print("hello world")

age=30
Age=20

print(age)
print(Age)

a=b=c=20
# camel case
myNameIs="Ayush"
# Snake case
My_Name_Is="Gupta"
# pascal case

print(myNameIs)
print(My_Name_Is)


#unpack collection
# A collection of values in a list , tuple ect Python allows yout to extract values 
fruits=["Apple","banana","Cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


#global variable without keyword

x="awesome"
def myFunct():
   print("python is "+x)
myFunct()

#with global keyword

def myFunc():
   global x
x="fantastic"

myFunc()


print("python is always  "+x)

# data type
# 4 data type

# Numeric data type

var1=1  #int data type
var2=True #bool data type
var3=10.023 #float data type
var4=10+3j #complex data type

print(var1)
print(var2)
print(var3)
print(var4)


#text type: str
# numeric type : int,float,complex

# sequence types :list,tuple,range

# replace method 
#replace a string with another string 
a='Hello, World'
print(a.replace("H","l"))


#split method
# return a list where the text between the specified separator becomes the list items 

print(a.split(","))

#concatenation method

b="Kaise ho"
c="ji"
d=b+" "+c
print(d)

#format string
# we cannot print number and string like this 
# age=35
# txt="my name is Ayush" + age
# print(txt)
#we can combine strings and numbers by using f-strings or the format() method
#we use f word

age=36
txt=f"my surname is gupta i am {age}"
print(txt)

#python Booleans
def myFunction():
   return True
print(myFunction())









