from array import *
'''
vals=array('i',[4,5,6,8,-5])

print(vals)
print(vals.buffer_info())

newArr=array(vals.typecode,(a for a in vals))
print(newArr)

#with While loop

i=0
while i < len(newArr):
    print(newArr[i])
    i+=1

a=list(vals)
a.sort()
print(a)

#Value from user and search

arr=array('i',[])
n=int(input("Enter the range of an array: "))
for i in range(n):
    x=int(input("Enter the next value: "))
    arr.append(x)
print(arr)

val=int(input("Enter the value you want to search: "))
k=0
for e in arr:
    if e == val:
        print(k)
        break
    k=k+1
#or we can do

print(arr.index(val))

arr=array('i',[])
rang = int(input("Enter the range of an array: "))
for i in range(rang):
    val=int(input("Enter the next value: "))
    arr.append(val)
print(arr)
#Without using in-built function
arr=array('i',[10,20,30,40,50])

l=2
k=0
for i in arr:
    if k==l:
        k = k + 1
        continue
    else:
        print(i)
   k = k + 1
#With in-built function
arr.pop(2)
print(arr)


#reverse without using function
a=-1
b=0
arr=array('i',[10,20,30,40])
arr1=array('i',[])
for i in arr:
    c=a-b
    arr1.append(arr[c])
    b=b+1
print(arr1)

#reverse  with function

arr.reverse()
print(arr)
'''
