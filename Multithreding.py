#When you breakdown the bigger task into small parts it's called multithreading
#If you run now multi apps in mobile or laptop each are running on different CPU cores, cores are called threding
#It improves the performance of an app and also saves the tinme of execution

#Thread module
#syntax = thread.start_newthread(Function,args[kwargs])

from threading import  *
import time
from time import *
'''
def cal_sqre(nums):
    print("Calculate the square of the num")
    for n in nums:
        sleep(0.3)
        print("square is :", n*n)
def cal_cube(nums):
    print("Calculatete the cube of the num")
    for n in nums:
        sleep(0.3)
        print("Square of num:", n*n*n)

arr = [3,5,4,7]
t1=time()
cal_sqre(arr)
cal_cube(arr)
print("Total time take by function to execute :", time() - t1)

#-----------------------------------------------------------------------------------

#Threding Module
#There are 3 methods
#1. start() - It is used to initiate the thread and it is called once by each thread so execution can begin
#2. run() - this method is used to define thread activity & override the class that inherent the thread class
#3. join() - this method is used to stop the other execcution untill the thread terminates

#declaration thread paramter :
# It contain the target function and it's argument to be passed

#ex
def print_hello(n):
    print("Hello, how old are you ?", n)

Thread(target = print_hello(n), args=(18,))
'''


def cal_sqre(nums):
    print("Calculate the square of the num")
    for n in nums:
        sleep(0.3)
        print("square is :", n*n)
def cal_cube(nums):
    print("Calculatete the cube of the num")
    for n in nums:
        sleep(0.3)
        print("Square of num:", n*n*n)

arr = [2,5,6,7]

t = time()
th1 = Thread(target=cal_sqre,args=(arr,))
th2 = Thread(target=cal_cube,args=(arr,))


th1.start()
th2.start()

th1.join()
th2.join()

print(" Total time taking by threads is :", time() - t) # print the total time
print(" Again executing the main thread")
print(" Thread 1 and Thread 2 have finished their execution.")


#or we can use run

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)

t1 = hello()
t2 = Hi()

t1.start()
sleep(0.5)
t2.start()


t1.join()
t2.join()

print("Bye")