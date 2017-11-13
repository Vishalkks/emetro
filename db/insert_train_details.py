import sqlite3
conn = sqlite3.connect('Emetro.db')


#train_info purple and green line
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT001','Mysore Road','Baiyappanahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT002','Mysore Road','Baiyappanahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT003','Mysore Road','Baiyappanahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT004','Mysore Road','Baiyappanahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT005','Mysore Road','Baiyappanahalli','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT006','Mysore Road','Deepanjalinagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT007','Mysore Road','Attiguppe','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT008','Mysore Road','Vijaynagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT008','Mysore Road','Hosahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT009','Mysore Road','Magadi Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT010','Mysore Road','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT011','Mysore Road','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT012','Mysore Road','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT013','Mysore Road','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT014','Mysore Road','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT015','Mysore Road','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT016','Mysore Road','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT017','Mysore Road','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT018','Mysore Road','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT019','Mysore Road','Swami vivekananda Road','Purple')")


conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT020','Deepanjalinagar','Attiguppe','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT021','Deepanjalinagar','Vijaynagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT022','Deepanjalinagar','Hosahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT023','Deepanjalinagar','Magadi Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT024','Deepanjalinagar','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT025','Deepanjalinagar','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT026','Deepanjalinagar','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT027','Deepanjalinagar','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT028','Deepanjalinagar','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT029','Deepanjalinagar','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT030','Deepanjalinagar','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT031','Deepanjalinagar','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT032','Deepanjalinagar','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT033','Deepanjalinagar','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT034','Attiguppe','Vijaynagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT035','Attiguppe','Hosahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT036','Attiguppe','Magadi Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT037','Attiguppe','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT038','Attiguppe','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT039','Attiguppe','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT040','Attiguppe','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT041','Attiguppe','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT042','Attiguppe','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT043','Attiguppe','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT044','Attiguppe','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT045','Attiguppe','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT046','Attiguppe','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT047','Vijaynagar','Hosahalli','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT048','Vijaynagar','Magadi Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT049','Vijaynagar','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT050','Vijaynagar','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT051','Vijaynagar','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT052','Vijaynagar','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT053','Vijaynagar','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT054','Vijaynagar','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT055','Vijaynagar','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT056','Vijaynagar','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT057','Vijaynagar','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT058','Vijaynagar','Swami vivekananda Road','Purple')")


conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT059','Hosahalli','Magadi Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT060','Hosahalli','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT061','Hosahalli','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT062','Hosahalli','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT063','Hosahalli','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT064','Hosahalli','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT065','Hosahalli','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT066','Hosahalli','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT067','Hosahalli','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT068','Hosahalli','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT069','Hosahalli','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT070','Magadi Road','City Railway Station','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT071','Magadi Road','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT072','Magadi Road','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT073','Magadi Road','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT074','Magadi Road','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT075','Magadi Road','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT076','Magadi Road','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT077','Magadi Road','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT078','Magadi Road','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT079','Magadi Road','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT080','City Railway Station','Majestic','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT081','City Railway Station','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT082','City Railway Station','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT083','City Railway Station','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT084','City Railway Station','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT085','City Railway Station','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT086','City Railway Station','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT087','City Railway Station','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT088','City Railway Station','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT089','Majestic','Sri M Vishweshwarayya','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT090','Majestic','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT091','Majestic','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT092','Majestic','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT093','Majestic','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT094','Majestic','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT095','Majestic','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT096','Majestic','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT097','Sri M Vishweshwarayya','Vidha Saudha','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT098','Sri M Vishweshwarayya','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT099','Sri M Vishweshwarayya','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT100','Sri M Vishweshwarayya','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT101','Sri M Vishweshwarayya','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT102','Sri M Vishweshwarayya','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT103','Sri M Vishweshwarayya','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT104','Vidha Saudha','Cubbon Park','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT105','Vidha Saudha','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT106','Vidha Saudha','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT107','Vidha Saudha','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT108','Vidha Saudha','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT109','Vidha Saudha','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT110','Cubbon Park','MG Road','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT111','Cubbon Park','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT112','Cubbon Park','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT113','Cubbon Park','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT114','Cubbon Park','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT115','MG Road','Trinity','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT116','MG Road','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT117','MG Road','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT118','MG Road','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT119','Trinity','Halasuru','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT120','Trinity','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT121','Trinity','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT122','Halasuru','Indiranagar','Purple')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT123','Halasuru','Swami vivekananda Road','Purple')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('PT124','Indiranagar','Swami vivekananda Road','Purple')")


print("Opened database successfully")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT001','Putennahalli','Nagasandra','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT002','Putennahalli','Nagasandra','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT003','Putennahalli','Nagasandra','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT004','Putennahalli','Nagasandra','Green')")


conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT005','Putennahalli','JP Nagar','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT006','Putennahalli','Banashankari','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT007','Putennahalli','Rashtreeya Vidyalaya Road','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT008','Putennahalli','Jayanagar','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT009','Putennahalli','Southend Circle','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT010','Putennahalli','Lalbagh','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT011','Putennahalli','National College','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT012','Putennahalli','K R Market','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT013','Putennahalli','National College','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT014','Putennahalli','Chickpete','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT015','Putennahalli','Majestic','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT016','Putennahalli','Mantri Square','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT017','Putennahalli','Srirampura','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT018','Putennahalli','Kuvempu Road','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT019','Putennahalli','Rajajinagar','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT020','Putennahalli','Mahalakshmi','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT021','Putennahalli','Sandal Soap Factory','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT022','Putennahalli','Yeshwantpur','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT023','Putennahalli','yeshwantpur Industry','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT024','Putennahalli','Peenya','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT025','Putennahalli','Peenya Industry','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT026','Putennahalli','Jalahalli','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT027','Putennahalli','Dasarahalli','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT028','Putennahalli','Nagasandra','Green')")

conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT006','JP Nagar','Banashankari','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT007','JP Nagar','Rashtreeya Vidyalaya Road','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT008','JP Nagar','Jayanagar','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT009','JP Nagar','Southend Circle','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT010','JP Nagar','Lalbagh','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT011','JP Nagar','National College','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT012','JP Nagar','K R Market','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT013','JP Nagar','National College','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT014','JP Nagar','Chickpete','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT015','JP Nagar','Majestic','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT016','JP Nagar','Mantri Square','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT017','JP Nagar','Srirampura','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT018','JP Nagar','Kuvempu Road','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT019','JP Nagar','Rajajinagar','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT020','JP Nagar','Mahalakshmi','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT021','JP Nagar','Sandal Soap Factory','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT022','JP Nagar','Yeshwantpur','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT023','JP Nagar','yeshwantpur Industry','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT024','JP Nagar','Peenya','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT025','JP Nagar','Peenya Industry','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT026','JP Nagar','Jalahalli','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT027','JP Nagar','Dasarahalli','Green')")
conn.execute("INSERT INTO train_info (train_id, source, destination, line) VALUES ('GT028','JP Nagar','Nagasandra','Green')")



print("Opened database successfully")

conn.commit()
#station_info table
#purple line mysore road to majestic
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P001','Mysore Road',2,1)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P002','Deepanjalinagar',2,2)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P003','Attiguppe',2,3)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P004','Vijaynagar',2,4)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P005','Hosahalli',2,5)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P006','Magadi Road',2,6)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P007','City Railway Station',2,7)")


conn.commit()
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P008','Majestic',4,8)")


print("Opened database successfully")
#purple line majestic road to baiyappanahalli
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P009','Sri M Vishweshwarayya',2,9)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P010','Vidha Saudha',2,10)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P011','Cubbon Park',2,11)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P012','MG Road',2,12)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P013','Trinity',2,13)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P014','Halasuru',2,14)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P015','Indiranagar',2,15)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P016','Swami vivekananda Road',2,16)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('PT001','P017','Baiyappanahalli',2,17)")
print("Opened database successfully")

conn.commit()
#Green line puttenhalli to majestic
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G001','Puttenahalli',2,1)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G002','JP Nagar',2,2)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G003','Banashankari',2,3)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G004','Rashtreeya Vidyalaya Road',2,4)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G005','Jayanagar',2,5)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G006','Southend Circle',2,6)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G007','Lalbagh',2,7)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G008','National College',2,8)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G009','K R Market',2,9)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G010','Chickpete',2,10)")
conn.commit()
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G011','Majestic',4,11)")
print("Opened database successfully")
#Green line majestic to nagasandra
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G012','Mantri Square',2,11)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G013','Srirampura',2,12)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G014','Kuvempu Road',2,13)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G015','Rajajinagar',2,14)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G016','Mahalakshmi',2,15)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G017','Sandal Soap Factory',2,16)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G018','Yeshwantpur',2,17)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G019','yeshwantpur Industry',2,18)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G020','Peenya',2,19)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G021','Peenya Industry',2,20)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G022','Jalahalli',2,21)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G023','Dasarahalli',2,22)")
conn.execute("INSERT INTO station_info(train_id, station_id, station_name, no_of_platforms, point) VALUES ('GT001','G024','Nagasandra',2,23)")
conn.commit()
print("Opened database successfully")

#train_schedule	
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT001','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:00')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT002','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:10')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT003','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:20')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT004','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:30')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT005','G001','Puttenahalli', 1,'G024','Nagasandra', 2,'12:40')"\
			)
#vijaynagar to mg road schedule
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT054','P004','Vijaynagar', 1,'P012','MG Road', 2,'12:40')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('GT022','G002','JP Nagar', 1,'G018','Yeshwantpur', 2,'12:40')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT095','P008','Majestic', 1,'P015','Indiranagar', 2,'12:40')"\
			)



			
print("Opened database successfully")		
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT001','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:00')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT002','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:10')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT003','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:20')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT004','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:30')"\
			)
conn.execute("INSERT INTO train_schedule(train_id, src_station_id, source,src_platform,dest_station_id,destination,dest_platform,departure_time)\
			VALUES ('PT005','P001','Mysore Road', 2,'P017','Baiyappanahalli', 1,'04:40')"\
			)
print("Opened database successfully")
conn.commit()