import sqlite3

#Creating connection to save the values into table
# It won't create same db again. If the db exists it will make the connection to that.
connection = sqlite3.connect("my_friends.db") 

#create cursor object. It will allocate some memory to execute the queries.
c = connection.cursor()

#execute some sql
c.execute("CREATE TABLE nonrelatives (first_name TEXT, last_name TEXT, closeness INTEGER);")

#commit changes
connection.commit()

#closing the connection
connection.close() 