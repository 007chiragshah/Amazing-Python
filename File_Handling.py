#For this key function is open()
#open() takes two arguments : 1. Filename, 2. Method or mode
#There are 4 modes :
#1. "r" - read - used to read the file, gives an eroor if file does not exist
#2. "a" - append - opens a file for appending, creates the file if does not exist
#3. "w" - write - opens a file to write, creates the file if not exist
#4. "x" - create -- Creates the file, gives an error if file exist

#file should be handled as binary and text
#1. t = text, this is the default value
#2. b = binary or image

#Syntax  : f = open("filename") -- to read the file, only filename is enough
#or f = open("filename", "rt") -- r for read and t for text but it's an optional as its byfefault value

#ex
'''
f = open("demo.txt")
#print(f.read())      #for reading all data
print(f.readline())   #read only first line
print(f.readline())   #read second line
print(f.read(5))      #pass only 5 char

#for loop

for i in f:
    print(i)

#Once we read the file need to close the same
f.close()


#Write to the file

#a  = append -- to write in an existing file
#w  = Write -- overwrite the file

f = open("demo1.txt", "a")             #it will create the file as it's not exist
f.write("Hello handsome hung chirag")



f1 = open("demo1.txt", "w")      #will overwrite the demo1 file
f1.write("Hayeeeee  oyeeeeee")

f2 = open("demo1.txt", "r")
f2.read()




#Copy the file

f = open("demo.txt", "r")
f1 = open("demo2.txt", "w")

for i in f:
    f1.write(i)




#Copy image file as not required to read

f = open("20150507_175015.jpg", "rb")
f1 = open("image.jpg", "wb")

for i in f:
    f1.write(f)



#create the file

#f3 = open("demo3.txt", "x")     #create the blank file
f4 = open("demo4.txt", "w")     #create the file if not exist
f5 = open("demo5.txt0", "a")    #create the file if not exist




#remove the file -- for that need to import the os module

from os import  *

remove("demo3.txt")   #removes files
rmdir("myfolder")     #removes dire

'''

from os import *

if path.exists("demo2.txt"):
    remove("demo2.txt")
else:
    print("File Not Exist")