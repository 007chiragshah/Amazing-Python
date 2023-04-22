#IT means that function calling from it self


import sys
'''
sys.setrecursionlimit(2000)      #To set the new recurrsion limit
print(sys.getrecursionlimit())   #To get the recurrsion limit
i=0
def greet():
    global i
    i+=1
    print("Hello", i)
    greet()                   #This is called recursion as function is calling itself from function
greet()


#-------------------------------------------------------------------------------



#Fectorial using Recurrsion

def fect(n):
    if n == 0:
        return 1

    return n * fect(n-1)

result = fect(4)
print(result)


#-------------------------------------------------------------------------------

'''