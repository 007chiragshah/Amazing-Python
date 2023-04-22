#OOPs stands for object oriented programing

#In real world everything is an object
#There are 2 things in every object
#1. Attributes or Variable (An object knows something)
#2. Behaviour or Methods or Fucntions (An objece do something)

#variables are used to store tha data and methods are used to defing the behaviour of an object.

#Class is an user defined prototype from which objects are created.

## Class and Objects :

#Class is a blue print that create the object
#Integer, float etc are built in type where by using class we can create own type
#Class can be defined by using class keyword and class name like -- class class_name():

#Class consist of 2 things : 1. Attribute (Variable) and 2. Behaviour (Methods/Function).

#We can call any methods from class but the behaviour of evry object is different so we have to be specific of define
#for which object we are calling the method

#So we need to pass and object in it as parameter at the time of calling the method

#Way of calling method : class_name.methond_name(Variable)

#Example
'''
class computer:                     #created the class computer

    def config(self):               #defines the method(function)
        print("i5, 16GB, 1TB")

com1 = computer()                     #assign or store the value in variable
print(type(com1))                   #checck the type of user defined class

a= 9                                #check the type of built in class
print(type(a))

computer.config(com1)               #calling a method config from class computer for variable com1

#here com1 is parameter so while we calling the method config variable pass in it as parameter which goes in to the self.
#So self is the object that we are passing

#Another method of calling method

com1.config()  #Here we already defines that config and com1 belongs to computer
               #Here we directly mentined that for which object we are calling the method so that that object will pass
               #as an argument and goes into the self


#-----------------------------------------------------------------------------------------------------------------------


#2. __init__ method


#1. in python varisbles are defined into a special method know as __init__ method.
#2. This method works similary constructor in other methods.
#3. No need to call init method like other as it is get called automatically.
#4. this methods get called atleast once with every object so if you have 2 objets it will get called twice.
#5. We can pass an argument to class in the construcor it self, values of an argument will be accepted in class on the init
#method as an parameter.
#6. the variable name of an object is get passed automatically and accepted by the self in init method.
#7. There is no need to give name as self, we can give any name but we have to give some name.

#Ex

class computer:

    def __init__(self):                  #defining the method init
        print("In Init")

    def config(self):
        print("i5, 16 GB, 1TB")

com1 = computer()
com2 = computer()

com1.config()
com2.config()                              #here you can see we are not calling init method

#so while you run this yuo can see we get the "in init" twice without calling it.
#it is because init is called automatically and once with one object and here we have two object hence it called twice.


#----------------------------------------------------------------------------------------------



#Init with and argument

class computer():

    def __init__(self,cpu,ram):  #passing an object argument in init as parameter

        self.cpu = cpu           #variables are assigned with an object as self represent the name of an object
        self.ram = ram           #object name automatically gets assigned to self

    def config(self):
        print("Config is :",self.cpu, self.ram)  #here we need to define the variables with self as these are not the
                                                 #local variables, as it is attached with an object hence we need to
                                                 #define it with an object self as object name goes in to self automatically.


com1 = computer("i5",16)      #here we have assigned value as an argument but you see there is only 2 arguments but
com2 = computer("Rysen",8)    #in init it accepting 3 so it because the object name will assigned to self automatically
                              #so it's also 3 arguments

com1.config()
com2.config()


#-----------------------------------------------------------------------------------------------------------------------



#Constructor and Self

#All the objects are stored into a heap memory
#Size of an object depends upon the variable and size of eaxh variable
#Now question is who allocate the size and the ans is constructor.

#ex

class person:

    def __init__(self):
        self.name = 'Chirag'
        self.age = 27

    def compare(self,other):         #in this we need to take care that self will be assigned to that variable which is
        if self.age == other.age:    #calling the fucntion and other will be refer to another variable
            return True              #in our case c1 will refer to self as it is calling the function and c2 will refer
        else:                        #the other
            return False


c1=person()
c2=person()

c1.name='Rashi'
c1.age=30

if c1.compare(c2):            #compare is not by default so we have created the function
    print("They are same")
else:
    print("They are not same")


print(c1.name)    #here 1st run the code without any change in name then apply above syntax of change the name and then check
print(c2.name)    #here we will get same outpur as we are passing single argument in init for 2 object


#Also we can compare the variables by defines the compare function


#-----------------------------------------------------------------------------------------------------------------------



#Special Variable

#1. Instance Variable - this variables are different for each object so if change variable for one object will not effect
                        #others
#2. Class(Static) Variable - This variables are same for all object so when we change this it will affect all the objects.

#ex

class car:

    wheels = 4                    #Class (static) Variable

    def __init__(self):
        self.motor = 'BMW'          #Here we have created one value for 2 cars
        self.mil = 16



car1 = car()
car2 = car()

print(car1.motor, car1.mil, car.wheels)   #while run this will get the same output for both the object car1 and car2
print(car2.motor, car2.mil, car.wheels)   #We can also call the class variable (wheels) by an object but we are prefers
                                          #this because it's an class variable and will same for all the objects

car1.motor = 'Tata'               #Now changing the value of instance variable motor for object car 1
print()

print(car1.motor, car1.mil, car.wheels)   #Now you can the value for car 1 is changed and its not affect on other object
print(car2.motor, car2.mil, car.wheels)   #car2


#Now change the value for wheels from 4 to 5 and run this code again and you will see that value for wheels will channge
#for both the object car1 and car2


#---------------------------------------------------------------------------------------------------------------------



#Different type of methods

#1. Instance Method - Work with the instance variables
    #It has 2 types : 1. Accessors (getters) - will use to fetch the values of instance variable
    #                 2. Mutators (setters) - will use to modify the value of instance variable
    #for this method we are using self key word.

#2. Class method - Work with the class variables.
    #for this method need to use class key word which is 'cls'
    #In this method to get the output we need to use decorators before method start as @classmethod

#3. Static Method - This method has not any concerned with any type of variable instance or class.
    #Use - This method is use when we are calling a method from different module which has not concerned with any type of
    #      varibales. let's say we are calling method for finding fectorial number
    #In this method alson we need to use the decorators as @staticmethod

#Ex

class student:

    school = 'Telusko'   #Class variable

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

#1. Instance method
    #Avg method is instance method as it will work with instance variables
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #2 type of instance method
    #Accessor (getters) method - this method use to fetch the value of instance variable
    def get(self):
        return self.m1

    #Mutator (setters) method - this method use to modify the value of instance variable
    def set(self,value):
        set.m1 = value


#2. Class method
    @classmethod     #need to use decorators before class method else will get the error while calling this method
    def getschool(cls):  #here you can see we have used class keyword cls as it's class method
        return cls.school

#3. Static method
    @staticmethod   #need to use this decorator befor static method
    def info():
        print("This is school... from abc module")  #use thos method will use when we need to call any method from other
                                                    #module which has not any concern with any type of variables like
                                                    #method to find the fectorial number

s1 = student(85,90,95)
s2 = student(94,95,99)

print(s1.avg())               #calling Instance method
print(student.getschool())    #Calling class method
print(student.info())         #calling static method


#-----------------------------------------------------------------------------------------------------------------------



#Inner Class
#you can create an object of inner class inside the outer class
#or
#you can create an object of inner class outside the outer class and call it by outer class name

#ex

class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()          #1st method to call the inner class value

    def show(self):
        print(self.name, self.rollno)   #another method of printing instance variable
                                        #this show method is for student information
        self.lap.show()

    class Laptop:    #Inner class

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)   #this show method will use to print laptop value

s1 = student("chirag",1)
s2 = student("Disha",30)

print(s1.show())


#-----------------------------------------------------------------------------------------------------------------------



#Inheritance

#What is inheritance :
#                       for ex if we have 1 class with some methods and now we want to creat the another class with some
#new features and also want to inheritant the features from existing class it's call inheritance.

#   then the old class which inheritent in new class called super class and new class will be called as child/sub class
#of that super class

#There are 3 methods : 1. Single level inheritant, 2. Multilevel inheritant, 3. Multiple inheritant

#ex

class A:                                #as we have used class A as inheritant in class B so it's call super/parent class.
    def feature_1():
        print("feature 1 is working")

    def feature_2():
        print("feature 2 is working")

#1. Single level inheritant

class B(A):         #we have used class A as inhertance so while calling we can see the methods from class A also
    def feature_3():
        print("feature 3 is working")

    def feature_4():
        print("feature 4 is working")

#2. Multilevel inheritance

class C(B):     #Here we are inheritant the features of class B only but as B is already inheritant the class A so we can
                #see the methods of class A also while calling class C and it's called multilevel inheritance
    def feature_5():
        print("feature 5 is working")


#3. Multiple inheritance

class D:

    def feature_6():
        print("feature 6 is working")

class E:
    def feature_7():
        print("feature 7 is working")

#here you can see class D and class E is indipendent with it's own features but in class F we want to inheritant for both
#class D and class E and it's called multiple inheritance

class F(D,E):           #Multiple inheritant
    def feature_8():
        print("feature 8 is working")


a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()
f1 = F()

#single level inheritant
#here you can see methods from class A and class B as A is inheritant of class A.
print(b1.feature_1())     #from class A
print(b1.feature_3())     #from class B

#Multilevel inheritance.
#here you can see methods from class A and class B and class C.
print(c1.feature_2())     #from class A
print(c1.feature_4())     #from class B
print(c1.feature_5())     #from class C

#Multiple inheritant
#here you can see methods from class D and class E in F even though both are not inheritant
print(f1.feature_6())     #from class D
print(f1.feature_7())     #from class E
print(f1.feature_8())     #from class F



#-----------------------------------------------------------------------------------------------------


#Constructor in inheritance

class A:
    def __init__(self):
        print("In init A")

    def feature_1():
        print("Feature 1 from Class A")

class B(A):
    def feature_1():
        print("Feature 1 from class B")

#Here you can see we have not mentioned init method in class B and class A is super class of class B
#Now when you call class B it first check if class B has constuctor init method or not if not then it will jump to class
#A and will print the constructor of class A
#But if we have defined constructor in class B the it will print the constructor from class B

b1=B()
print()

#-----------------------------------------
#now what if we have constructor in class B too but we want to call constructor from class A then we need to use the
#method called super()

#ex
class A:
    def __init__(self):
        print("In init A")

    def feature_1():
        print("Feature 1 from Class A")

#By using super method we can call any methods also from super class
class B(A):
    def __init__(self):
        super().__init__()
        print("In init B")

    def feature_1():
        print("Feature 1 from class B")

b1 = B()
print()

#--------------------------------------------------------
#MRO - Method Resolution Order
#It always print from left to right

#ex
class A:
    def __init__(self):
        print("In init A")

    def feature_1():
        print("Feature 1 from Class A")

class B:
    def __init__(self):
        super().__init__()
        print("In init B")

    def feature_1():
        print("Feature 1 from class B")

#Now we have class C which has two super class A and B
#So what will be the outpur if we call super method from class C
# is it print cinstructor from super claas A or B or both, let's see
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In init C")

    def feature_1():
        print("Feature 1 from class B")

c1= C()

#here ouput will be constructor from Class A because as metioned above MRO is reading from left to right and super Class
#A is in left side and B in Right, if it not find the constructor in A then it will print constructor from class B.

#Same it works for the methods too


#------------------------------------------------------------------------------------------------------------------------


#Polymorphism

#let's break the word : poly == Many
#                        morph == form

#so this method means one thing can take many forms, for ex we human is a thing and we have different forns(behaaviour)
#in front of different people say front of friends behaving different, front of family is different etc

#There are 4 types :
#1. Duck Typing
#2. Operator Overloading
#3. Method Overloading
#4. Method overriding

#1. Duck Typing : There is one line is if there is a bird who walk like duck, swim like duck, fly like duck then it is a
#                 duck. Same way in this if our variable has let's execute then it doesn't matter which type we are
#                 assigning only matters is it should have execute

#ex
class Mycharm:
    def execute(self):
        print("compiling")
        print("Running")

class Myeditor:
    def  execute(self):
        print("Spell check")
        print("Covention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = Mycharm()     #assigning one type of ide to ide

lap1 = Laptop()
lap1.code(ide)      #here we need to pass ide in argument as need to get o/p of the ide type
print()
#Now we change the type

ide = Myeditor()
lap2=Laptop()
lap2.code(ide)

#as you see it doesn't matter what type we are passing only matters is that ide has that execute because all the type has
#execute methods.


#-------------------------------------------------


#2. Operator Overloading

#what and why use - The class which is by default in python say int, float, str etc has their default methods for different
#                   operators say + (__add__), - (__sub__) etc but when the class is user defined it doesn't know the
#                   what different operators are doing like +,-,* etc so it will give an error so for that we need to
#                   overload the methods for that operators.

#ex

class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):     #overriding the __add__ method for class student
        m1 = self.m1 + other.m1
        m2 = self.m1 + other.m1
        m3 = student(m1,m2)
        return m3

    def __gt__(self, other):        #overriding the gt '>' method for class student
        g1 = self.m1 + self.m2
        g2 = other.m1 + other.m2
        if g1 > g2:
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(self.m1,self.m2)  #as s1 is calling __Str__ we need to return in this way

s1 = student(70,80)
s2 = student(80,80)

#now we want to add the marks of students
s3 = s1 + s2

print(s3.m1)   #so run this without defining the method it will give an error that "TypeError: unsupported operand type(s)
#              for +: 'student' and 'student'" as class student don't know what '+' operatot is doing.

#Once we override the __add__ method for class student it will the correct output

#Same we have done for greater than '>' operator

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

#for ex if variable a has some vlue and when we print the a will get the value in output but
#while we print s1 we are getting object name and it's address in output
#behing the scene both are calling __str__ method so for s1 we need to override the method

a = 9
print(a)
print(s1)


#------------------------------------------------------


#3. Method Overloading -

#When you have 2 same methods with same but different parameters in one class known as method overloading.
#In python we cannot create 2 methods with same name and same parameters in one class so will use some trick for this

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s= a+b
        else:
            s=a

        return s

s1 = student(50,40)

print(s1.sum(5,9))

#Here we have created sum function in such a way that if user enters 3,2 or 1 argument it will work because in python
#we can not create the same function with same name and different parameters but in other languages we can.


#------------------------------------------------
#4. Method overriding

#When you have 2 same methods with same and same parameters in one class known as method overriding.
#In python we cannot create 2 methods with same name and same parameters in one class so will use some trick for this

class A:
    def show(self):
        print("In A Show")

class B(A):
    def show(self):
        print("In B show")

s1 = B()

print(s1.show())     #when you run this you will get B object has no attribute show

#now do class B inheritant to class A and then run this you will get output "In A show" as class B access all feature of A

#now define the show method in class B and then run the code
#The moment you defin the same method in class B and when you call class B it will override the method from Class A.


#---------------------------------------------------------------------------------------------------------------------
'''
