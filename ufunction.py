#It's called Universal Function
from numpy import *
'''
#addition by python built in function zip

x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=[]

for i, j in zip(x,y):
    z.append(i+j)
print(z)

#-------------------------------------------------------------------------------

#Create Function

def myadd(x,y):
    return x+y

myadd=frompyfunc(myadd, 1,1)
print(myadd([1,2,3,4],[5,6,7,8]))

#-----------------------------------------------------------------------------


#Simple Arithmatic

arr1=array([1,2,3,4])
arr2=array([5,6,7,8])
arr11=array([-1,-2,-3,-4])

arr3=add(arr1,arr2)               #Addtion
arr4=subtract(arr2,arr1)          #Subtraction
arr5=multiply(arr1,arr2)          #Multiply
arr6=divide(arr1,arr2)            #Divide
arr7=power(arr1,arr2)             #power
arr8=mod(arr1,arr2)               #mod
arr9=remainder(arr1,arr2)         #Reminder
arr10=divmod(arr1,arr2)           #Quotient and Mod -- here output will give 2 array (1. Quotient and 2.Mod)
print(absolute(arr11))            #Absolute


print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)


#-------------------------------------------------------------------------------------------


#Rounding the values

#Below are the 5 methods which are used for rounding off

arr1 = trunc([-3.166666,3.66667])
arr2 = fix([-3.166666,3.66667])
arr3 = around(3.16667, 2)
arr4 = floor([3.1666, 3.66666])
arr5 = ceil([3.1666, 3.66666])

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)

#----------------------------------------------------------------------------------


#Log

#logBase2

arr1 = log2([1,10])
arr2 = log10([1,10])
arr3 = arange(1,10)

print(arr1)
print(arr2)
print(log(arr3))

#-----------------------------------------------------------------------------------


#Summation Over an Axis

arr1=array([1,3,5])
arr2=array([2,4,6])

arr3=sum([arr1,arr2])               #Sum will do the summation of both the array
arr4=sum([arr1,arr2], axis=1)       #This will sum the array individually
arr5=cumsum([arr1])                 #This will give cumulative sum (1, 1+3, 1+3+5)

print(arr3)
print(arr4)
print(arr5)

#------------------------------------------------------------------------------------


#Product

arr1=array([1,3,5])
arr2=array([2,4,6])

arr3=prod([arr1])                    #Prod will do the multiplication of whole arr (1*3*5)
arr4=prod([arr1,arr2])               #Sum will do the multiplication of both the array (1*3*5*2*4*6)
arr5=prod([arr1,arr2], axis=1)       #This will multiplication the array individually (1*3*5) and (2*4*6)
arr6=cumprod([arr1])                 #This will give cumulative product (1, 1*3, 1*3*5)

print(arr3)
print(arr4)
print(arr5)
print(arr6)



#--------------------------------------------------------------------------------------------


#Differences

arr1=array([1,3,5])

arr3=diff([arr1])          #it will give the discrete difference (3-1, 5-3)
arr4=diff([arr1], n=2)     #here n  value define the times of difference here n=3 so it will do (3-1=2, 5-3=2) and (2-2=0)

print(arr3)
print(arr4)

#-------------------------------------------------------------------------------------------



#Finding LCM (Lowest Common Multiple)

#1 --- Individual
num1 = 4
num2 = 6

Result=lcm(num1,num2)

print(Result)     #Output will be 12 because this is lowest common mul of both value (4*3=12 and 6*2=12)



#2  ---- Array
arr = array([1,4,5,7])

arr1=lcm.reduce(arr)     #reduce method is used to calculate LCM for whole array
print(arr1)              #output wil be 140 because it will be LCM of all array (1*140=140, 35*4=140, 28*5=140, 20*7=140)


#3 ----- Range
newarr = arange(1,11)

print(lcm.reduce(newarr))  #it will calculate LCM of given raange.

#---------------------------------------------------------------------------------------



#Finding GCD -- Greatest Common Denominator

num1 = 6
num2 = 4                   

result=gcd(num1,num2)      #Output will be 2 because this is GCD of both value (6/2=0 and 4/2=0)

print(result)


#2  ---- Array
arr = array([20,8,32,16])

arr1=gcd.reduce(arr)     #reduce method is used to calculate GCD for whole array
print(arr1)              #output wil be 4 because it will be GCD of all array (20/4=0, 8*4=0, 32/4=0, 16/4=0)


#3 ----- Range
newarr = arange(1,11)

print(gcd.reduce(newarr))  #it will calculate LCM of given raange.



#Set Operations

#Create

arr=array([1,2,2,3,3,3,3,4,4,4,5,1,1,6,7])

arr1=unique(arr)   #Unique function is used to find the unique values from the array
print(arr1)


#2. Unique from 2 Arrays  --- UnionID

arr2=array([1,1,1,2,2,2,3,4,5,5,6])
arr3=array([6,6,68,8,9,10,11,11,12])

arr4=union1d(arr2,arr3)
print(arr4)

#3 Common from both the array --- Intersection

arr5=array([1,1,2,3,4,4,5])
arr6=array([2,4,4,5,7,8])

arr7=intersect1d(arr5,arr6)

print(arr7)

'''
