import sqlite3

# Connection between python script and database.db to execute what in python script in db
connection = sqlite3.connect("database.db")

# we executed the script in scheme.sql in database.db
with open('scheme.sql') as f:
    connection.executescript(f.read())

# make interaction between the db and python script
cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )
# Commit the changes
connection.commit()
# Close the connection
connection.close()