-----guides to use this project------

locate the database folder and follow the steps bellow.

1.in the database folder, find db_settup.py and:
	(a): rename the "DB_NAME" to whatever you wish
	(b): rename the table in TABLES[]
	
2. find the db_connector.py and:
	(a): rename the server, mine is "localhost"
	(b): provide the password if there's one
	(c): define the port, mine is "3306" as default
	(d): database name, should be added after the following last step.

after the above configuration, run the db_setup.py file in order to create
the database. afterwords, add the database name to (d), in step two above and
then run the file. this should work smoothly.

if the above steps ran without errors, you can now run the app.py file to 
start using the application, otherwise, follow the steps carefully 
and try again.
