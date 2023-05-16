#F String

#this method is for single or double variable but if we have multiple variables then this is not correct method
#method 1
name = "chirag"
surname = "shah"
print("this is %s"%name)

#method 2
print("This is {} {}".format(name,surname))
#or
print("This is {1} {0}".format(surname,name))

#method 3
print(f"this is {name} {surname} {4*5} rocks")

