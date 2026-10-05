import sqlite3
con=sqlite3.connect('person.db')
con.execute('create table if not exists person (id int primary key,name varchar(20),age int) ')

# i=int(input("enter the id:"))
# n=input("enter the name:")
# a=int(input("enter the age:"))
#                                     # placeholder ?
# e=con.execute('insert into person (id,name,age)values(?,?,?)',(i,n,a))

# con.commit()

# read operation
i=int(input("enter the id:"))
e=con.execute('select * from person where id=?',(i,))
print(e.fetchall())