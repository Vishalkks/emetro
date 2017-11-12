import sqlite3
conn = sqlite3.connect('Emetro.db')
print("Opened database successfully")
conn.execute('CREATE TABLE train(id VARCHAR(8) NOT NULL primary key,source VARCHAR(20),destination VARCHAR(20),platform VARCHAR(5), line VARCHAR(20),time VARCHAR(10))')
print("Table created successfully")
conn.close()
