#This method is used when we are getting an errors
#There is 3 type of an error :
# 1. Compile Error - this error will get when we are compiling the code, let's say if is there any syntax error will come
#                     when we run the code.
# 2. Logical Error - this error will come when if we have any wrong output instead of excepting something else
# 3. Runtime Error - This error will come in between the code is running, let's say inbetween code we asked use to give
#                    an input but user gives an wrong input then will get this error.
'''
#ex
a=5
b=0

print(a/b)   #this will give the error as we all know we cannot device any number by 0
print("bye") #this will come in output when all the code executed

#run above code and you will get an error and also not getting "bye" in o/p is because at the moment you got an error
#python will stop further execution so we will use the special block say "try" and "Except" to handles such error and
#prevent from stopping exceution in between



#ex
a=5
b=0
try:
    print(a/b)   #Will use try only where we feels that this is critical statement and might give some error
except Exception as e:  #here we are using "as error" to print the message from error message, you can name anything than error
    print("you cannnot devide the value by 0", e) #also we need to print an error here so need to use e

print("Bye")



#resource closing - resourse can be anything say file, database connection etc

#One thing make sure if you have opened the resource then you are the one who has to close that, but if we put the command
#for closing the resource in try block then when error  comes it will not execute this command and will jump outof the
#loop and resource will stay open and viceversa.

#so for that we are using a special block named finally- this block will execute even if we are getting an error or not
#so we will execute the resourse close command in finally block.

#here we will use print as file handling topic is still pending

a=5
b=0

try:
    print("Resource Open")
    print(a/b)
except Exception as e:
    print("You have an error :",e)

finally:
    print("Resorse closed")

#you can also check by giving the valid value in b

#now we are pring the valid message as we knows the error but what if we have print the message in Exception for orher
#error and we got the other so for that if we know the error we can except the Exception for that perticular value
#then will print the general message in else block

'''
a=5
b=2
try:
    print(a/b)
    n = int(input("Enter the num :"))
except ZeroDivisionError as e:
    print("You can not devide value by 0 :",e)
except ValueError as e:
    print("Invalid input :",e)
except Exception as e:
    print("Something went wrong ",e)