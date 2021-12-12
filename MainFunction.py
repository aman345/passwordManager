from PasswordGenerator import generateStrongPassword
from PasswordDataBasemanager import DatabaseOperations
from datetime import datetime
import os
import pandas as pd
def generateCsvOFdb(data):
    df = pd.DataFrame(data)
    df.to_csv("exported.csv")

if __name__=='__main__':
    #gui section goes here
    password = generateStrongPassword(8)
    database = DatabaseOperations()
    data = database.showtableData()
    generateCsvOFdb(data)
    
