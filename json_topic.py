#json is stands for javascript object nation
#it is easy to learn and most effective way to interchange the data.
#json mainly supports 6 types of data types:
#1. string, 2. Number, 3. Boolean, 4. Object, 5. Null, 6. Array
#json representation is similar to the python directory
#Python to json known as serialization and json to python known as deserialization

#2 methods for serialization - 1. dump() -accept two arguments one is data to be serialize and sec is file to which write the data
#                              2. dumps() - accept only one argument is data to be serialize

#ex
'''
#1. dumps() :
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
with open("data.json","w") as write_file:
    json.dump(x,write_file)


#2. dump():

import json
student = {
  "name": "Chirag",
  "age": 30,
  "gf": "Disha Patani",
  "rank": 1
}

print(json.dumps(student))


#----------------------------------------------------------------------------------

#Examples
#python to json
import json
print(json.dumps({"name": "john", "age":30}))    #Dict      to Object
print(json.dumps(["Apple", 105]))                #list      to Array
print(json.dumps(("Apple","Banana")))            #Tupple    to Array
print(json.dumps("Hello Swxy"))                  #String    to string
print(json.dumps(42))                            #int       to number
print(json.dumps(40.50))                         #float     to number
print(json.dumps(True))                          #True      to true
print(json.dumps(False))                         #False     to false
print(json.dumps(None))                          #None      to null


#------------------------------------------------------------------------------
'''
import json

#Json to Python
#2 methods for deserialization : 1. load() - used to read from file and convert it to python object
#                                2. loads() - used for only deserialize the string data

student = '{"Name": "John", "Age": 30}'
print(json.loads(student))


#Format, order and seperate the result

import json
person = {
  "Name": "Chirag",
  "Age": 27,
  "Married": True,
  "Divorced": False,
  "Pet": None,
  "Children": ("Ann","Belly"),
  "Car": [{"Motor": "BMW 123", "Mil": 20},
          {"Motor": "TATA", "Mil": 30}
          ]
}

#print(json.dumps(person))   #It will bit confusing to read
#print(json.dumps(person, indent=2))     #using indentation
#print(json.dumps(person, indent=2, separators=(", ", ": ")))  #Seperator Coma and Space for each object and :, space to
#                                                             to seperate keys from values
print(json.dumps(person, indent=2, sort_keys=True))  #to sort we will use sort_keys