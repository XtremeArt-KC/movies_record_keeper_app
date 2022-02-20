import mysql.connector
from mysql.connector import errorcode

from db_connector import cursor

print("")
print("===============================")
print("Welcome to the database setup!!")
print("to create new database, edit this")
print("file and change the DB_NAME to")
print("any name you want.")
print("")
print("To continue, press any key")
input("then press enter: ")
print("===============================")
print("")

DB_NAME = 'assignment_1'

#initialize tables as an empty dictionary
TABLES = {}


TABLES['movie_records'] = (
                  "CREATE TABLE `movie_records` ("
                  " `u_id` int(11) NOT NULL AUTO_INCREMENT,"
                  " `title` varchar(255) NOT NULL,"
                  " `customer` varchar(255) NOT NULL,"
                  " `comments` varchar(255) NOT NULL,"
                  " `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
                  " PRIMARY KEY (`u_id`)"
                  ") ENGINE=InnoDB"
                  )


#this function checks if a database with the provided name exists
#then creates a new database in the mysql database server.
def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("")
    print ("Successfully created database {}".format(DB_NAME))
    print("")


# this function creates a table in the selected database
def create_tables():
    print("")  
    cursor.execute("USE {}".format(DB_NAME))
    
    for tbl_name in TABLES:
        tbl_description = TABLES[tbl_name]
        
        # check if a table with same name exists in the database before creating
        try:
          print("---------------------------")
          print("Creating table ({}) ".format(tbl_name), end="")
          cursor.execute(tbl_description)
          print("---------------------------")
          print("")
        except mysql.connector.Error as error_101:
          if error_101.errno == errorcode.ER_TABLE_EXISTS_ERROR:
              print("   : ----> Sorry table already exists")
              print("---------------------------")
              print("")
          else:
              print(error_101.msg)  

# calling create_database function 
create_database()

# calling the create_table function
create_tables()