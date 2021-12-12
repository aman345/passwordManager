#create a sqlite db
import sqlite3
from sqlite3 import Error
from datetime import datetime
class DatabaseOperations:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('passwordmanager.db',check_same_thread=False)
            if self.conn is not None:
                self.cur = self.conn.cursor()
                self.cur.execute("CREATE TABLE IF NOT EXISTS passwordManagerTable( _id INTEGER PRIMARY KEY,"
	                    +"tag TEXT NOT NULL,"+
	                    "user_name TEXT  NULL,"+
	                    "email TEXT NULL ,"+
	                    "password TEXT NOT NULL ,"+
	                    "website_url TEXT NOT NULL ,"+
	                    "created_on TEXT NOT NULL,"+
	                    "updated_on TEXT null);")   
                print("Database created successfull")
            else:
                print("Error! cannot create the database connection.")
            
        except Error as e:
            print(e)
        finally:
            self.conn.commit()
    

    def insertPassword(self,tag,user_name,email,password,website_url):
        self.cur.execute('INSERT INTO passwordManagerTable(tag,user_name,email,password,website_url,created_on,updated_on) VALUES(?,?,?,?,?,?,?)',(tag,user_name,email,password,website_url,datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
        self.conn.commit()
        return True

    def updatePassword(self,_id,password):
        self.cur.execute('UPDATE passwordManagerTable SET password = '+password+',updated_on = '+datetime.now().strftime("%m/%d/%Y, %H:%M:%S")'+ WHERE _id =='+ _id)
    
    def deletePassword(self,_id):
        self.cur.execute('DELETE FROM passwordManagerTable WHERE id =='+ _id)

    def showtableData(self):
        return self.cur.execute('Select * from passwordManagerTable')

    
