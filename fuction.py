'''
#Basic function

def myfunction():
    print("Hello")
    print("Good Morning")

myfunction()


#Add Function
def add():
    x=5+4
    print(x)

add()



#Add with argument

def add(x,y):
    c=x+y
    print(c)

add(5,4)



#Return value

def add(x,y):
    c=x+y
    return c

result = add(5,4)
print(result)



#Two operation in one function

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2 = add_sub(5,4)
print(result1, result2)



#Argument in Function

#Unmutable

def update(x):
    x=8
    print("x " ,x)

a=10
update(a)

print("a ",a)


#Mutable

def update1(lst):
    lst[1]=25
    print(lst)

lst=[10,15,20]
update1(lst)

print(lst)

#-----------------------------------------------------------------------------------


#Arguments in Function

#1. Position

def person(name,age):
    print(name)
    print(age-5)

person('Chirag',26)    #Here we set the position correctly so will get the proper output
person(26,'Chirag')    #Here we have interchanged the position so will get the error for age



#2 Keyword

def person(name,age):
    print(name)
    print(age)

person(age=26,name='Chirag')   #Here if we don't know the position we can provide the value with key in actual arguments



#3 Default

def person(name,age=18):      #Here we have mentioned the default value 18 for age
    print(name)
    print(age)

person('Chirag',26)           #HEre we have given the input of age so it will print that in output
person('chirag')              #Here we have not given the age in argument so it will print the default value 18 in age



#4. Varieable Length

def person(name,*data):     #Here we have mentioned *data as we dont know how many argument will be passed
    print(name)
    print(data)             #HEre we will get the output in tuple
#or
    print(name)
    for i in data:           #Using for loop
        print(i)

person('Chirag',26,'Una',94286)  #Chirag will pass in name and rest of info will pass in data



#5. Keyworded veriable length

#There is one issue in variable length is we dont know the value comes in data is represnt to what
#So we will use the key while passing the value while calling the function
#For that we need to use ** in formal argument
def person(name,**data):          #** for keyworded variable
    print(name)
    print(data)
#or
    print(name)                  #USing for loop
    for i,j in data.items():     #data.items use to pass key and value in i and j respectively
        print(i, j)

person('chirag',age=26,City='Una',Mob=94286)


#Global Variable

#1. Without local variable

a = 10    #--------  Global variable we can use this variable anywhere in any function.

def something():
    print("In Function", a)

something()
print("Out  function", a)   #Here we will get the same output as we havent use any other variable so function will use the
                            #global variable by default.



#2. With local variable
a = 10    #--------  Global variable we can use this variable anywhere in any function.

def something():
    a=15       #--------------------Local variable that we can use only with the given function
    print("In Function", a)

something()
print("Out  function", a)  #Here we will get two different o/p for inside function we got the local variable o/p
                        #and for out side function we got the global variable o/p

#Note that the first priority always been given to the local variable.


#3 Global variable inside function
a=10       #--------------- Global variable
def something():
    global a     #------- Defining global variable inside function, so it will treat as global
                 #Now we can change the value of a it will change the value of global variable
                 #If we are not declaring a as global inside function and if we change the value of a it will be trate as a local
    a=15
    print("In Function", a)
something()
print("Out Function", a)   #Here value for global is also changed as we have declared the variable as global inside the function



#4. To use the same variable as global and local inside the function

a=10

def something():
    a=15
    print("In function", a)

    globals()['a'] = 20 #Here we need to use function called globals() to change the value of global variable

#By using globals() we can access all the globals variable or we can use perticular  by defining the name in [''].

something()
print("Out Fun", a)


#-----------------------------------------------------------------------------------------------
#List with the Function

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[10,20,33,43,53,30,63,40]

even,odd = count(lst)

print("Even: {} and Odd: {}".format(even,odd))

#---------------------------------------------------------------------------------------

#Fectorial using function

def fect(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

result = fect(4)
print(result)

#----------------------------------------------------------------------------------------------
'''

