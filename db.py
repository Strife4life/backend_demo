import sqlite3
#connect to database
conn = sqlite3.connect('users.db')
#create a cursor
c = conn.cursor()
#create a table
#c.execute("INSERT INTO users VALUES ('3201', 'password')")
#print("command executed successfully")

#query the database
c.execute("SELECT * FROM users")

print(c.fetchall())


#commit the command
conn.commit()
#close our connection
conn.close()

