from PasswordGenerator import generateStrongPassword
from PasswordDataBasemanager import DatabaseOperations
import pandas as pd
database = DatabaseOperations()
def passwordChoiceUtility():
    password = ""
    choice = input("Use AutopasswordGen(y) or userdefined(n):> ")
    if choice == 'y' or choice == 'Y':
        lenght = input("Enter Length of password:> ")
        password = generateStrongPassword(length=int(lenght))
    else:
        password = input("Enter User Defined Password:")
    return password
def generateCsvOFdb(data):
    df = pd.DataFrame(data)
    df.to_csv("exported.csv")

def addContact():
    print("[+] Adding Details[+]")
    tag = input("Enter tag:>")
    user_name = input("username:>")
    email = input("email:> ")
    password = passwordChoiceUtility()
    website_url = input(r"""Enter website url or address""")
    return database.insertPassword(tag,user_name,email,password,website_url)

def updatePassword():
    print("[+]Updating password[+]")
    ids = int(input("id:>"))
    password = passwordChoiceUtility()
    return database.updatePassword(ids,password)

def deletePassword():
    print("[+]Deleting Password[+]")
    ids = input("Id:")
    database.deletePassword(ids)

def showTable():
    rows  = database.showtableData()
    print("{:>10}{:>10}{:>10}{:>20}{:>20}{:>20}{:>20}{:>20}".format(*["_id","tag","user_name","email","password","website_url","created_on","updated_on"]))
    for i in rows:
        print("{:>10}{:>10}{:>10}{:>20}{:>20}{:>20}{:>20}{:>20}".format(*i))
def exitfun():
     database.conn.commit()
     exit()
def choice(ch):
        switcher={
                0:exitfun,
                1:addContact,
                2:updatePassword,
                3:deletePassword,
                4:showTable}
        return switcher.get(ch,"Invalid choice")
if __name__=='__main__':
  
    __header__ =  r"""
             --    _____                                           _   __  __                                            _____                           _       
             --   |  __ \                                         | | |  \/  |                                          / ____|                         | |      
             --   | |__) |__ _  ___  ___ __      __ ___   _ __  __| | | \  / |  __ _  _ __    __ _   __ _   ___  _ __  | |      ___   _ __   ___   ___  | |  ___ 
             --   |  ___// _` |/ __|/ __|\ \ /\ / // _ \ | __|/ _`| | |\/| | | / _` || '_ \  / _` | / _` | / _ \| __|  | |     / _ \ |  _ \ / __| / _ \ | | / _ \
             --   | |   | (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| | | |  | || (_| || | | || (_| || (_| ||  __/| |    | |____| (_) || | | |\__ \| (_) || ||  __/
             --   |_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_| |_|  |_| \__,_||_| |_| \__,_| \__, | \___||_|     \_____|\___/ |_| |_||___/ \___/ |_| \___|
             --                                                                                      __/ |                                                       
             --                                                                                     |___/                                                        """
    print(__header__)
    print("[+] Password manager Application [+]") 
    #this is going to be a console based application 
    switcher={
                0:exit,
                1:addContact,
                2:updatePassword,
                3:deletePassword,
                4:showTable}
    while(True):
        print("[1]Add New Entry        [+]")
        print("[2]Update Existing Entry[+]")
        print("[3]Delete Entry         [+]")
        print("[4]Display Table        [+]")
        print("[0]Exit                 [+]")
        ch = input(":>>>>")
        choice(int(ch))()
    
