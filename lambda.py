#A function without name is known as annonymous function or lambda function
#Instead of defining function before we can define it whenever we want to use that.
#That time we need to use the lambda keyword while defining the function.
#Function will pass into the function as its an object in python.
#In lambda you can pass the n number of arguments but only can pass the single expression.

'''
#1. Square of number

f= lambda a: a*a

result = f(5)
print(result)

#2. Addition of number

add = lambda b,c : b+c
result = add(5,6)
print(result)

#----------------------------------------------------------------------------------------


#Filter, Map and Reduce using Lambda

from functools import reduce

#1. Filter

#Find evens

nums=[2,4,6,9,7,1,5,8,10]
evens = list(filter(lambda n: n%2==0,nums))  #Filter is a by default function which takes 2 args, 1 is function 2 is iterable
print(evens)

#2. Map

#Double the values which are in evens
doubles = list(map(lambda n: n*2,evens)) #map is a by default function which takes 2 args, 1 is function 2 is iterable
print(doubles)

#3. reduce

#this function we need to import from functool
#sum all the value but 2 values at a time

sum= reduce(lambda a,b: a+b,doubles)
print(sum)

#-------------------------------------------------------------------------------
'''
