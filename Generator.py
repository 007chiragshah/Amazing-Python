#Generator will generate the iterator without the iter function
#yield is the special keyword is used in function that make your fucntion as generator

#ex
#here we define the function not a class
def gen():

    yield 5     #yield is also returning the value

val = gen()
print(val)    #same as iterator it will print the object so,
print(val.__next__())   #this will print the value

#need to print the perfect square of topten

def topten():
    n=1
    while n<=10:
        sq = n*n
        yield sq    #yield will retunr the value but it will 1 by 1
        n += 1

vals = topten()
for i in vals:
    print(i)

#use = the use when you have 1000 records in database and you want to fetch them withour storing in mem at that time
#yield will be used to fetch them one by one
