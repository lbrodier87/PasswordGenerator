# PasswordGenerator
 Python code to generate random passwords. 
 
## RandomPassword_GUI.py
Tkinter GUI for password generator. Calls generatePwd() from RandomPasswordGenerator.py. 

## PwdGen_GUI.bat
bat file for launching the GUI on Windows (you can shortcut this file to desktop). 

## RandomPasswordGenerator.py
Contains main function for password generation generatePwd(), with following parameters
- length:int=12, length of generated password
- rep:int=1, number of password to generate
- lwrc:bool=True, include lowercase character set
- uprc:bool=True, include uppercase character set
- num:bool=True,  include numbers character set
- sym:bool=True, include symbols character set
- forceCheckContent:bool=True, ensure that there is at least one character for each selected charset
