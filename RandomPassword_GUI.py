#import libraries
import tkinter as tk
from tkinter import filedialog
from RandomPasswordGenerator import generatePwd
import os

#create main window and set name + icon
win = tk.Tk()
win.title("Password generator - v1.0")
win.iconbitmap("key.ico")

#generate password with user inputs and add to output text area
def doGenPwd():
    out_txt.delete('1.0', 'end') #reset output text area
    #errors handling
    if(int(pwd_len.get()) < 4):
        out_txt.insert('end', 'Error: \nPassword length must be at least 4.')
        return(0)
    if(lwrchar_bool.get() == False and upchar_bool.get() == False and num_bool.get()==False and sym_bool.get()==False):
        out_txt.insert('end', 'Error: \nAt least 1 character-set must be selected.')
        return(0)
    #generate password with input settings (returns a global variable)
    global currentpwd 
    currentpwd = generatePwd(int(pwd_len.get()), int(pwd_rep.get()), \
                      lwrchar_bool.get(), upchar_bool.get(), \
                        num_bool.get(), sym_bool.get(), force_bool.get())
    #add to output text area
    for p in currentpwd:
        out_txt.insert('end', p + "\n")
    #success return code = 1
    return(1)

#save generated pwd to a txt file 
def saveToTxtAs():
    #open save dialog in write mode with txt extension
    fw = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    #return if file is null
    if fw is None: 
        return
    #write passwords in separate lines
    for p in currentpwd:
        fw.write(p + "\n")
    #close file writer
    fw.close()
    #auto open file with os if option is checked
    if autoOpen_bool.get():
        os.startfile(fw.name)

## FRAME 1 - select character sets
frame1 = tk.Frame(win, relief=tk.RIDGE, borderwidth=1)
frame1.grid(row=0, column=0, sticky="nesw")

# Frame 11 - title
frame11 = tk.Frame(frame1)
frame11.grid(row=0, column=0, sticky='w')
f1_label = tk.Label(frame11, text="Include characters from:")
f1_label.grid(row=0, column=0, sticky="w")

#frame 12 - character sets checkboxes
frame12 = tk.Frame(frame1)
frame12.grid(row=2, column=0)

lwrchar_bool = tk.BooleanVar()
lwrchar_yn = tk.Checkbutton(frame12, text="lowercase", variable=lwrchar_bool)
lwrchar_yn.select()
lwrchar_yn.grid(row=1, column=0, sticky="W")

upchar_bool = tk.BooleanVar()
uprchar_yn = tk.Checkbutton(frame12, text="uppercase", variable=upchar_bool)
uprchar_yn.select()
uprchar_yn.grid(row=1, column=1, sticky="W")

num_bool = tk.BooleanVar()
num_yn = tk.Checkbutton(frame12, text="numbers", variable=num_bool)
num_yn.select()
num_yn.grid(row=2, column=0, sticky="W")

sym_bool = tk.BooleanVar()
sym_yn = tk.Checkbutton(frame12, text="symbols", variable=sym_bool)
sym_yn.select()
sym_yn.grid(row=2, column=1, sticky="W")

## FRAME 2 - additional options (force one + length + nb rep)
frame2 = tk.Frame(win, relief=tk.RIDGE, borderwidth=1)
frame2.grid(row=0, column=1, sticky="nesw")

#frame 21 - force option checkbox
frame21 = tk.Frame(frame2)
frame21.grid(row=0, column=0, sticky='nesw')

force_bool = tk.BooleanVar()
force_yn = tk.Checkbutton(frame21, text="force one from each charset", variable=force_bool)
force_yn.select()
force_yn.grid(row=0, column=0, sticky="W")

#frame 22 - password length and nb repetitions
frame22 = tk.Frame(frame2)
frame22.grid(row=1, column=0, sticky='nesw')

pwd_len_label = tk.Label(frame22, text="password length: ")
pwd_len_label.grid(row=0, column=0, sticky='w')
pwd_len = tk.Entry(frame22, width=10)
pwd_len.insert('end', 12) #default value
pwd_len.grid(row=0, column=1, sticky="W")

pwd_rep_label = tk.Label(frame22, text="repetitions: ")
pwd_rep_label.grid(row=1, column=0, sticky='w')
pwd_rep = tk.Entry(frame22, width=10)
pwd_rep.insert('end', 8) #default value
pwd_rep.grid(row=1, column=1, sticky="W")

## FRAME 3 - generate password + save as buttons
frame3 = tk.Frame(win)
frame3.grid(row=3, column=0, sticky='nesw', columnspan=2)

btn = tk.Button(frame3, text="Generate passwords", command = doGenPwd)
btn.grid(row=0, column=0, sticky='nesw', padx=1)

btn_saveas = tk.Button(frame3, text="Save as...", command=saveToTxtAs)
btn_saveas.grid(row=0, column=1, sticky='nesw', padx=10)

autoOpen_bool = tk.BooleanVar()
autoOpen = tk.Checkbutton(frame3, text="auto open saved file", variable=autoOpen_bool)
autoOpen.select()
autoOpen.grid(row=0, column=2)

## FRAME 4 - output text area
frame4 = tk.Frame(win)
frame4.grid(row=4, column=0, sticky='nesw', columnspan=2)
out_txt = tk.Text(frame4, width=45, height=10)
out_txt.grid(row=0, column=0, sticky='nesw')

#bring main window to front (run just before mainloop)
win.lift()
win.attributes('-topmost', True)
win.after_idle(win.attributes, '-topmost', False)

#start app main loop...
win.mainloop()