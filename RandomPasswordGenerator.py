import string
import random
import os

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = "1234567890"
symbols = "+-*%^~=&/\()[]{}?!@#.,_"

def generatePwd(length:int=12, rep:int=1, lwrc:bool=True, uprc:bool=True, num:bool=True, sym:bool=True, forceCheckContent=True):
    # error if pwd does not contain any character set... 
    if not lwrc and not uprc and not num and not sym:
        raise Exception("At leat one character set must be active...")
    
    # concatenate reference character sets to final character set
    charset = ""
    if lwrc:
        charset += lowercase
    if uprc:
        charset += uppercase
    if num:
        charset += numbers
    if sym:
        charset += symbols
     
    pwd = [] # list to store the passwords
    for i in range(rep): # repeat as many time as you need passwords
        # generate a new password until it get a valid password
        validPwd = False 
        while(validPwd != True):
            p = ""
            for j in range(length): 
                p += charset[random.randint(0, len(charset)-1)] #add a random character as many time as pwd length
            if(forceCheckContent): 
                validPwd = checkPwd(p, lwrc, uprc, num, sym) #function to check that pwd contain at least one of requested character categories
            else: 
                validPwd = True
        pwd.append(p)
    return(pwd)

def checkPwd(pwd:str, lwrc:bool=True, uprc:bool=True, num:bool=True, sym:bool=True):
    # count occurences of each character categories
    nb_lwrc = 0; nb_uprc = 0; nb_num = 0; nb_sym = 0
    for i in range(len(pwd)): 
        if pwd[i] in lowercase:
            nb_lwrc += 1
        if pwd[i] in uppercase:
            nb_uprc += 1
        if pwd[i] in numbers:
            nb_num += 1
        if pwd[i] in symbols:
            nb_sym += 1
    
    # if category was requested and is counte 0, the pwd is not valid
    if (lwrc and nb_lwrc == 0) or (uprc and nb_uprc == 0) or (num and nb_num == 0) or (sym and nb_sym ==0):
        valid = False
    else:
        valid = True
    return(valid)

if __name__ == "__main__":  
    # ask user pwd length and number of pwd to generate
    length = int(input("Longeur du mot de passe: "))
    rep = int(input("Nombre de mot de passe à générer: "))
    pwd = generatePwd(length, rep)
    
    # print result to user
    print("")
    for i in range(len(pwd)):
        print(pwd[i])
    print("")

    # wait for user to quit or save result to a file
    action = ""
    while (action != 'q'):
        action = input("q to exit / s to save: ")
        if(action == 's'):
            path = "passwords.txt"
            fw = open(path, 'w')
            for i in range(len(pwd)):
                fw.write(pwd[i] + "\n")
            fw.close()
            print("Passwords saved sucessfully to file 'passwords.txt' !")
            os.startfile(path)