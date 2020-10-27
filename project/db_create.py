import sqlite3 
from __config import DATABASE_PATH

try:
	with sqlite3.connect(DATABASE_PATH) as conn:
		c = conn.cursor()

		c.execute(""" 
			CREATE TABLE tasks(task_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
								name TEXT NOT NULL, due_date TEXT NOT NULL, priority INT NOT NULL, status INT NOT NULL)
			""")

		#insert dummy data 

		c.execute('INSERT INTO tasks(name,due_date,priority,status) VALUES("Finish this tutorial","11/05/2020", 10, 1)') #status 1 means open 
		c.execute('INSERT INTO tasks(name,due_date,priority,status) VALUES("Finish Real Python Course 2","11/05/2020", 10, 1)') 
except sqlite3.OperationalError as oe:
	print("An error occured : {}".format(oe))

