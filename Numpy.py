from numpy import *

'''
#Addition of an array
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])


#Add 5 to each element of an array
arr1= arr1 + 5 
print(arr1)


#Add two arrays
arr3 = arr1+arr2
print(arr3)

#------------------------------------------------------------

#Some mathematical functions

print(sin(arr1))    #find the sin
print(cos(arr1))    #find the cos
print(log(arr1))    #find the log
print(min(arr1))    #find the min

print(max(arr1))    #find the max

# Max without using built in function

arr1 = array([4,2,3])
if arr1[0] > arr1[1]:
    if arr1[0] > arr1[2]:
        print(arr1[0], " is great")
    else:
        print(arr1[2], "is great")
elif arr1[1] > arr1[2]:
    print(arr1[1], " is great")
else:
    print(arr1[2], " is great")
    
    
print(sum(arr1))    #find the sum
print(average(arr1))#find the average
print(concatenate([arr1,arr2]))#concatenate the arrays

#-------------------------------------------------------------------------------

#addition of two arrays using for loop

arr1 = array([1,2,3])
arr2 = array([4,5,6])
list=[]
j=0
for i in arr1:
    k=i+arr2[j]
    j=j+1
    list.append(k)
print(list)

#-------------------------------------------------------------------------
#Differnt methods for creating an array

#1. array()

arr=array([1,2,3,4],[5,6,7])
print(arr)

#methods
print(arr.dtype)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print(type(arr))

#2 linspace() : bydefault it will create 50 part if we not menttioned the 3rd element.
arr=linspace(0,15)
print(arr)


#3 Arange()
arr=arange(1,16,2)
print(arr)


#4logspace

arr=logspace(1,40,10)
print(arr)
print('%.2f' %arr[0]) #to get the value with only 2 decimal after point


#5 zeors - To get all the value of an array as zeros
arr=zeros(5) #5 is the range of an array
arr1=zeros(5,int) #with the type of data
print(arr)
print(arr1)

#6 ones - To get all the value of an array as one
arr=ones(5) #5 is the range of an array
arr1=ones(5,int) #with the type of data
print(arr)
print(arr1)



arr1 = array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print(arr1.dtype) # to know the type
print(arr1.ndim) # to know the dimentiones
print(arr1.shape) #to know the shap of an array
print(arr1.size) #to know the size of an array

arr2 = arr1.flatten() # to convert array to 1D from 2D
print(arr2)

arr3 = arr1.reshape(3,4) #to convert array to 3D from 2D
print(arr3)

#or

arr4 = arr1.reshape(2,2,3) #to get two 2d arrays from 1 2d array
print(arr4)


arr = array([1,2,3], ndmin=5)
print(arr)
print(arr.ndim)

#------------------------------------------------------------------------------

#Indexing of an array

#1. 1D Array
arr = array([1,2,3,4,5])
print(arr[0])  # will print the first element of an array
print(arr[-1])  #will print the last element of an array negative index


#2. 2D Array

arr = array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr[0,1])  #will print the second element of the 1st array
print(arr[1,4])  #will print the fifth element of the 2nd array



#3. 3D Array

arr = array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])

print(arr[1,0,2])
print(arr[0,1,2])

#-----------------------------------------------------------------------------------------

#Copy of an array

arr1 = array([1,2,3,4,5])

#by using this method we can copy the array but both will redirect to same array and address
#it's also called alising
arr2=arr1
print(arr2)
print(id(arr1))
print(id(arr2))


#Shallo Copy
#this copy method is depending on each other
#if you change the value in 1 array after it copied even thoug it will also change the same in second array.
arr2=arr1.view()
arr1[1] = 10
print(arr1)
print(arr2)



#Deep Copy
#this copy method is not depending on each other
#if you change the value of arr1 after copied then value for arr2 is not changed
arr2=arr1.copy()
arr1[2]=30
print(arr1)
print(arr2)

#----------------------------------------------------------------------------------------------

#Slicing of an Array

#1. 1D array

arr = array([1,2,3,4,5])

print(arr[1:4])



#2.  2D array
arr = array([[1,2,3,4],[5,6,7,8]])
print(arr[0, 1:3])
print(arr[1, 0:2])
# 2nd element from both the array
print(arr[0:2, 2])
print(arr[0:2, 1:4])

#-------------------------------------------------------------------------------------------


#Change the Datatype

arr=array([1.1,2.2,3.3])
arr1=arr.astype(int)
print(arr1)
print(arr1.dtype)


#----------------------------------------------------------------------------------------
#Spliting an array

arr=array([1,2,3,4,5,6])
arr1=array_split(arr,3)
arr2=array_split(arr,4)
arr3=array_split(arr,8)
print(arr1)
print(arr2)
print(arr3)

#----------------------------------------------------------------------------------

#Searching the array

arr = array([1,4,3,5,7])
x=where(arr == 3)    #Search number
y=where(arr%2 == 0)  #search even
z=where(arr%2 == 1)  #search Odd
k=searchsorted(arr,7) #searchsorted
l=searchsorted(arr,[1,2,3]) #searchsorted for multiple value
print(x)
print(y)
print(z)
print(k)
print(l)

#-------------------------------------------------------------------------------------

#sorting the array

arr = array([3,5,2,1,0])
print(sort(arr))  #sorting output
print(arr)  #Note: This method will retun the copy of an array with original array unchanged

arr1=array([[9,1,5],[7,3,4]])
print(sort(arr1))   #Sorting 2D array


#-------------------------------------------------------------------------------------

#Filtering an array

#we cam filter the array based on true and false

arr=array([41,42,43,44])
x=[True,False,True,False]

arr1=arr[x]
print(arr1)

#creating the filter
filter_arr=[]
for i in arr:
    if i > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)

'''
