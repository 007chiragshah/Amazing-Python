import mysql.connector

#connection to db we use connect method
'''
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Chirag@123")    #connecting the host

mycursor = mydb.cursor()     #cusrsor is used to run the query as it will point the query to db

mycursor.execute("show databases")    #execute comand will execute the given query

for i in mycursor:                     #to check the output will run the for loop and here instead of mycursor
    print(i)                           #you can use any variable

'''
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Chirag@123",database='college')  #connection db directly
mycursor = mydb.cursor()
#mycursor.execute("show tables")



#create table

#mycursor.execute("create table contact(Name varchar(50), number int(20))")
#mycursor.execute("insert into contact values('chirag',12345678)")

insert = "insert into contact values('dipen',123456789)"
sel = "select * from contact"

mycursor.execute(insert)
mycursor.execute(sel)

for i in mycursor:
    print(i)
