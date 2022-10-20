import sqlite3

#Creating connection to save the values into table
# It won't create same db again. If the db exists it will make the connection to that.
conn = sqlite3.connect("my_friends.db") 

#create cursor object. It will allocate some memory to execute the queries.
c = conn.cursor()

#execute some sql
c.execute("CREATE TABLE family (first_name TEXT, last_name TEXT, closeness INTEGER);")

#commit changes
conn.commit()

#closing the connection
conn.close() 
