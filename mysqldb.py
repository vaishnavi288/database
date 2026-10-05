import mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")

# # connection to the db server

# c=con.cursor()

# c.execute("create database  if not  exists mydb2")
#                                 #    no need to give .db extension
# print("database created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="mydb2")
c=con.cursor()
c.execute('''create table  if not exists employee (empid int primary key,name varchar(20),age int ,salary int,gender varchar(20),place varchar(20))''')
print("table created")


# c.execute('''insert into employee(empid,name,age,salary,gender,place)values(101,"anu",20,20000,"female","kmr"),
#                                                                            (102,"ram",23,30000,"male","ekm"),
#                                                                            (103,"priya",27,80000,"female","kochi"),
#                                                                            (104,"hari",26,100000,"male","ktvm"),
#                                                                            (105,"manu",24,40000,"male","kollam")''')

# con.commit()
# print("data inserted")

# read operation

# c.execute('select * from employee')
# k=c.fetchall()
# print(k)


# particular value

# c.execute('select * from employee where empid=101')
# k=c.fetchall()
# print(k)


# read  all record with atribute name ,age

# c.execute('select name,age from employee where empid=102')
# k=c.fetchall()
# print(k)


# read where salary between 20000 and 30000
# c.execute('select name from employee where salary between 20000 and 30000')
# k=c.fetchall()
# print(k)

# read between age 20 and 25 return name and age
# c.execute('select name ,age from employee where age between 20 and 25')
# k=c.fetchall()
# print(k)

# name with 3 letter start with A
# c.execute('select name from employee where name like "a__"')
# k=c.fetchall()
# print(k)

# employee record with place start with "E"
# c.execute('select * from employee where place like "e%"')
# k=c.fetchall()
# print(k)


# employee record having age 30 and age 25
c.execute('select * from employee')
