import sqlite3
conn = sqlite3.connect('Emetro.db')
print("Opened database successfully")


conn.execute("drop table train_schedule")
conn.execute("drop table train_info")
conn.execute("drop table station_info")





conn.execute('CREATE TABLE train_info(train_id varchar(10) primary key,\
       source varchar(100) not null,\
	   destination varchar(100) not null,\
	   line varchar(20) not null)'
	)

print("Table1 created successfully")	
conn.execute('CREATE TABLE station_info(train_id varchar(10),\
	   station_id varchar(10),\
       station_name varchar(100) not null,\
	   no_of_platforms integer not null,\
	   point integer not null,\
	   primary key(train_id,station_id),\
	   foreign key(train_id) references train_info(train_id))'
	)

conn.execute('CREATE TABLE train_schedule(train_id varchar(10),\
	   src_station_id varchar(10),\
       source varchar(30) not null,\
	   src_platform integer not null,\
	   dest_station_id varchar(10),\
	   destination varchar(30) not null,\
	   dest_platform integer not null,\
	   departure_time varchar(10) not null,\
	   primary key(train_id,src_station_id,dest_station_id),\
	   foreign key(train_id) references train_info(train_id),\
	   foreign key(src_station_id) references station_info(station_id),\
	   foreign key(dest_station_id) references station_info(station_id))'
	)

print("Table1 created successfully")
conn.close()
