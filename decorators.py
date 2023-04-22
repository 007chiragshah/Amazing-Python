#By using this we can add the new features to the existing function.
#we can change the behaviour of the functuin at the compile it self.
#In this we can pass the existing func as a argument to new func
#We can create the new function inside the function.

#Ex - We need to swap the varible when a<b while deviding but we don't have access to the existing so we need
#to use this method

#original function
'''
def div(a,b):
    print(a/b)      #Here we got a<b but we cannot modify original function as we dont have access to it

def smart_div(func):      #so we will use the decorator method, Passing funct as an argumenr

    def inner(a,b):        #Creating function inside the function
        if a<b:
            a,b=b,a        #Adding extra feature to exiting func by adding Confition if we get a<b then swap the variable
        return func(a,b)
    return inner

div=smart_div(div)          #Changing the behaviour of existing function at compile

div=div(3,12)

'''