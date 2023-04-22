#import _name_

'''

print("Hey" + __name__)

#When we run this you can see in o/p we get the module name of _name_
#This is because when __name__ is used in other module and we call in running file it will print the name of that module.

#------------------------------------------------------


print("Lets start the __name__ Module")

#Now if i run this two line i am also getting "Hello" and "Welcome User" in O/P
#but i want that only if my main module __name__ runs the first time
#so after if __name__ == "__main__": statement in _name_ file i am getting above line in o/p

'''

#suppose we have defined some randome function
from _name_ import add

def fun1():
    add()
    print("This is fun 1")

def fun2():
    print("this is fun 2")

def main():
    fun1()
    fun2()

main()

#This is also same as cal module in _name_ file
#we have import the _name_ for add fun but when you run this you can see we are getting all the fun as it is calling main
#but why we need to call the main as we only want the add function
#this is because we have not defined the statement that only when __name__=="__main__" then only main function need to call
#from that file
#here you can see we are getting module name instead of __main__ after _name_ function

#After we add the if statement we are only getting required function