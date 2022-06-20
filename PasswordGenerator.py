import random
import string

num = list(string.digits)
alp = list(string.ascii_lowercase) +list(string.ascii_uppercase)
specialCharacter = ["!","@","#","$","%","&"]
superContainer = [num,alp,specialCharacter]

def generateStrongPassword(length):
    password = ""
    for x in range(0,length):
        password+=random.choice(random.choice(superContainer))
   
    return password

  
