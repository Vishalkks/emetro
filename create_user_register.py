import sqlite3
conn = sqlite3.connect('Emetro.db')
print("Opened database successfully")

#conn.execute("drop table user_details")
conn.execute('CREATE TABLE user_details(user_id VARCHAR(50) primary key,\
	password VARCHAR(20),FirstName VARCHAR(80) not null,LastName VARCHAR(20),\
	email VARCHAR(100) not null,DateOfBirth CHAR(10) not null,\
	Street varchar(100) not null,\
	city varchar(20) not null,pincode integer(6) not null,mobileNo integer(10) not null,\
	walletBalance integer(4) not null)')


print("Table created successfully")
conn.close()
