import os 
from db_connector import cursor, db

clear = lambda: os.system("cls")

# this function initializes the application
def application():
    clear()
    print("---Movie Record Keeper---")
    print()
    print("------This program stores records of movies borrowed and bought from a movie shop------")
    print()
    print("<<<<<<<<---OPTIONS--->>>>>>>>")
    print()
    print("1: Enter new Record")
    print("2: View All Records")
    print("3: Delete A Record")
    print("4: Update A Record")
    print("5: Search for Record")
    print()
    
    while True:
        print()
        user_option = input("Select an option: ").lower()
        if user_option =="1" or user_option == "2" or user_option == "3" or user_option == "4" or user_option == "5":
            break
        
    if user_option == "1":
        # calling the add_record function with input to add records to database
        add_record(input("Add a new record (movie title): "), input("Add customer name: "), input("Comment (bought/borrowed): "))

    elif user_option == "2":
        print("")
        print("==============================================================================")
        # calling the get_records function to view all records available in the database
        get_records()    
        print("===============================================================================")
        print("")
    
    elif user_option == "3":
        print("")
        print("==================================")
        # calling the delete_record function to delete a record(depends on id)
        delete_records(tuple(input("Enter id of record to delete: ")))    
        print("===================================")
        print("")
        
    elif user_option == "4":
        print("")
        print("============================")
        # calling the update_record function to update a record(depends on id)
        update_records(input("Enter id the record to update: "), input("Edit the record: "))    
        print("=============================")
        print("")
        
    elif user_option == "5":
        print("")
        print("============================")
        # calling the get_record function to get a specific record(depends on id)
        get_record(input("Enter id of the record: "))    
        print("=============================")
        print("")
        
            
        
# -----funtions for specific tasks--------
        
# this function creates a new record in the database 
def add_record(title, customer, comments):
    clear()
    print("")
    sql = ("INSERT INTO movie_records(title, customer, comments) VALUES (%s, %s,%s)")
    cursor.execute(sql, (title, customer, comments))
    db.commit()
    record_id = cursor.lastrowid
    
    print("")
    print("============================")
    print("Successfully added record {}".format(record_id))
    print("============================")
    print("")
    go_back()
    
# this function fetches all the records from the database 
def get_records():
    clear()
    sql = ("SELECT * FROM movie_records ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
    go_back()   
        
# this function deletes records in the database 
def delete_records(id):
    clear()
    sql = ("DELETE FROM movie_records WHERE u_id = %s")
    cursor.execute(sql, (id))
    db.commit()
    print("Record deleted successfully...")
    go_back()
    
# this function updates records in the database 
def update_records(id, title):
    clear()
    sql = ("UPDATE movie_records SET title = %s WHERE u_id = %s")
    cursor.execute(sql, (title, id))
    db.commit()
    print("Record updated successfully...")
    go_back()
    
# this function fetches a  record from the database 
def get_record(id):
    clear()
    sql = ("SELECT * FROM movie_records WHERE u_id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    print("-----------------------------")
    for row in result:
        print("---> ", row)
    go_back()


# a function to resume the home(main) application
def go_back():
    while True:
        print()
        go_back = input("Press (x) ,then press Enter to exit/go back: ").lower()
        if go_back == "x":
            application()
            break

# calling the application() funtion to run the app
application()