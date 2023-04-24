# PasswordGenerator
Python code to generate random passwords, with selectable length, character sets, and the option to save to a \*.txt file. 

Simply use the following command to launch the app: 
`python RandomPassword_GUI.py`
 
## RandomPassword_GUI.py
Tkinter GUI for password generator that uses the function *generatePwd()* from the file *RandomPasswordGenerator.py*. 

Call this file in python to launch the GUI: `python RandomPassword_GUI.py` 

## RandomPasswordGenerator.py
Contains main function for password generation ***generatePwd()***, with following parameters: 
- **length**:int=12, length of generated password
- **rep**:int=1, number of passwords to generate
- **lwrc**:bool=True, include lowercase character set
- **uprc**:bool=True, include uppercase character set
- **num**:bool=True,  include number character set
- **sym**:bool=True, include symbol character set
- **forceCheckContent**:bool=True, ensure that there is at least one character for each selected charset

Contains the function ***checkPwd()*** used to check that at least one character from each selected character set is present in the generated passwords. This function is used by *generatePwd()* if argument *forceCheckContent* is set to True (default). 

This file can be executed from the command line with reduced options: 
- Prompt user for *length* and *rep* arguments. 
- All four character sets are used. 
- Force at least one character from each set is True. 

## PwdGen_GUI.bat
Optional bat file for launching the GUI on Windows (you can edit and shortcut this file to desktop). 
