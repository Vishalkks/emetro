import sqlite3
conn = sqlite3.connect('Emetro.db')
print("Opened database successfully")

#conn.execute("drop table user_details")
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


#train_info purple and green line
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT001','Mysore Road','Baiyappanahalli','Purple');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT002','Mysore Road','Baiyappanahalli','Purple');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT003','Mysore Road','Baiyappanahalli','Purple');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT004','Mysore Road','Baiyappanahalli','Purple');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT005','Mysore Road','Baiyappanahalli','Purple');')

conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT001','Putennahalli','Nagasandra','Green');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT002','Putennahalli','Nagasandra','Green');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT003','Putennahalli','Nagasandra','Green');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT004','Putennahalli','Nagasandra','Green');')
conn.execute('INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT005','Putennahalli','Nagasandra','Green');')



#station_info table
#purple line mysore road to majestic
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P001','Mysore Road',2,1)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P002','Deepanjalinagar',2,2)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P003','Attiguppe',2,3)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P004','Vijaynagar',2,4)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P005','Hosahalli',2,5)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P006','Magadi Road',2,6)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P007','City Railway Station',2,7)')

conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P008','Majestic',4,8)')

#purple line majestic road to baiyappanahalli
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P009','Sri M Vishweshwarayya',2,9)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P010','Vidha Saudha',2,10)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P011','Cubbon Park',2,11)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P012','MG Road',2,12)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P013','Trinity',2,13)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P014','Halasuru',2,14)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P015','Indiranagar',2,15)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P016','Swami vivekananda Road',2,16)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P017','Baiyappanahalli',2,17)')



#Green line puttenhalli to majestic
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G001','Puttenahalli',2,1)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G002','JP Nagar',2,2)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G003','Banashankari',2,3)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G004','Rashtreeya Vidyalaya Road',2,4)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G005','Jayanagar',2,5)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G006','Southend Circle',2,6)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G007','Lalbagh',2,7)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G008','National College',2,8)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G009','K R Market',2,9)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G010','Chickpete',2,10)')

conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G011','Majestic',4,11)')

#Green line majestic to nagasandra
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G012','Mantri Square',2,11)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G013','Srirampura',2,12)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G014','Kuvempu Road',2,13)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G015','Rajajinagar',2,14)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G016','Mahalakshmi',2,15)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G017','Sandal Soap Factory',2,16)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G018','Yeshwantpur',2,17)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G019','yeshwantpur Industry',2,18)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G020','Peenya',2,19)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G021','Peenya Industry',2,20)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G022','Jalahalli',2,21)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G023','Dasarahalli',2,22)')
conn.execute('INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G024','Nagasandra',2,23)')



#train_schedule	
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('GT001','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:00 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('GT002','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:10 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('GT003','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:20 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('GT004','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:30 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('GT005','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:40 ')\
			')
			
			
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('PT001','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:00 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('PT002','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:10 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('PT003','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:20 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('PT004','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:30 ')\
			')
conn.execute('INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station,destination,dest_platform,departure_time)\
			VALUES ('PT005','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:40 ')\
			')

			
conn.close()