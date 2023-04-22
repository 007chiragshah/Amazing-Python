from numpy import *

m = matrix('1,2 ; 3,4 ;5,6')
print(m)

#or

arr=array([[1,2,3,4],[5,6,7,8]])

m=matrix(arr)
print(m)

# Addition and Multiplication of 2 matrix

m1 = matrix('1,2,5;3,4,6;5,6,8')
m2 = matrix('1,2,3;4,5,6;7,8,9')

m3= m1+m2 #Addition
m4= m1*m2 #Multiplication

print(m3)
print(m4)