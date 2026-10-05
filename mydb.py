import sqlite3

con=sqlite3.connect("company.db")

command="""create table if not exists employee(empid int primary key,
                                               name varchar (30),
                                               age int,place varchar (30) ,
                                               gender varchar(10),
                                               designation varchar(30),
                                               salary int)"""

# # primary key field used to identify  particular record
# # it must be unique /no duplicated value

con.execute(command)
# # con.commit()
# # print("table created")


# # # # insert operation
# command="""insert into employee(empid ,name ,age ,place,gender,designation,salary )
#          values(101,"anu",20,"kmr","f","dev",20000),
#          (102,"ammu",20,"ekm","f","dev",90000),
#          (103,"arun",20,"tvmr","m","dev",50000),
#          (104,"rose",20,"kochi","f","dev",10000)"""
# con.execute(command)
# con.commit() 
# print("data inserted succesfully")


# # #READ OPERATION
# # command="select * from employee"
# # # To read all employee records with all the attributes
# e=con.execute("select * from employee")
# print(e.fetchall())


# # all employee records with (returns names,age)
# e=con.execute("select name,age from employee")
# print(e.fetchall())

# print()

# # employee details with empid=101
# e=con.execute("select * from employee where empid=101")
# print(e.fetchall())

# print()


# # employee records with empid=101(return name,age)
# e=con.execute("select name,age from employee where empid=101")
# print(e.fetchall())

# # read all employee having age>=25 and salary <30000
# e=con.execute("select * from employee where  age>=25 and salary <30000")
# print(e.fetchall())

# read all empyee record withn empid other than 102

# e=con.execute("select * from employee where empid!=102")
# print(e.fetchall())


# read all emp record where place =ekm or age<=25

# e=con.execute('select * from employee where place="ekm" or age<=25')
# print(e.fetchall())


# # between

# # read where salary between 20000 and 30000
# e=con.execute('select * from employee where salary between 20000 and 30000')
# print(e.fetchall())

# # read between age 20 and 25 return name and age

# e=con.execute('select name,age from employee where age between 20 and 25')
# print(e.fetchall())


# like
# pattern matching
#  % 0 or more character
# _ exactly one character


# name start with R
# e=con.execute("select * from employee where name like 'R%'")
# print(e.fetchall())


# name with 3 letter start with A

# e=con.execute("select * from employee where name like 'A__'")
# print(e.fetchall())


# employee record with place start with "E"

# e=con.execute("select * from employee where place like 'E%'")
# print(e.fetchall())


# employee record having 3 letter place name ending with letter "m"

# e=con.execute("select * from employee where place like '__%M'")
# print(e.fetchall())


# employee record having age <25 and name start with letter "A"

# e=con.execute("select * from employee where age < 25 and  name like 'A%'")
# print(e.fetchall())







# in 

# employee record having age 30 and age 25

# e=con.execute("select * from employee where age in (20 and 30)")
# print(e.fetchall())

# order by

# e=con.execute("select * from employee order by name")
# print(e.fetchall())

# decending order

# e=con.execute("select * from employee order by name desc")
# print(e.fetchall())

# decending order by age

# e=con.execute("select * from employee order by age desc")
# print(e.fetchall())


# distinct (remove duplicate)

# e=con.execute("select distinct (place) from employee")
# print(e.fetchall())


# update

# con.execute("update employee set name='kiran',age=25 where empid=102")
# con.commit()
# print("update successfully")


# # delete
# con.execute("delete from employee where empid=103")
# con.commit()
# print("delete sucessfully")


