#A method which has only declaration but not the definition is called abstract method
#And the class which has abstract method called as Abstract Class.
#We cannot create an object from abstract classes
#Python by default does not supports the abstract class and abstract method so we need to import ABC (abstract base class)
#and abstract method from abc module
#abstract class should have atleast one abstract method
from abc import ABC, abstractmethod

class Computer(ABC):   #Class computer inheritant the ABC to make self as abstract class
    @abstractmethod    #to declare abstract method we need to use the decorator
    def process(self):
        pass           #This is abstract method as it only has the declaration but not any defination

class Laptop(Computer):
    def process(self):
        print("It's running")


class whiteboard(Computer):               #we have define this class without abstract method so it will give an error when
    def write(self):            #call it
        print("it's writing")

class programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

#com1=Computer()
#com1.process()         #when you run this cod you will get an error as we can not call the object from abstractmethod

lap = Laptop()
lap.process()           #It will print the process o/p

#white = whiteboard()
#white.process()         #It will give an error as there is not any abstract method called process so we need to inherintant
                        #it with abstract class
prog1=programmer()
prog1.work(lap)    #so it's mwndatory to have atleast one abstract method for abstract class