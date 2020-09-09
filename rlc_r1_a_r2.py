# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:15:47 2020

@author: Aranganathan
"""
from tkinter import *
from tkinter import ttk
import random

from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
key=2 #change the key for different time
def calculate():
        
     try:
         if E0.get():
             if len(E0.get()) != 9:
                  messagebox.showwarning("Alert","Please enter 9 digit roll number")
             else:
                roll_number=int(E0.get())
                random.seed(roll_number*key)
                R1=random.randint(20,40)
                A=random.randint(2,15)
                A=A*5
                R2=random.randint(15,51)
                messagebox.showinfo("Value","The Values for Roll number {} is \n Resistance R1 : {} Ohms \nGain A : {} \nResistance R2 : {} K Ohms".format(roll_number,R1,A,R2))  
         else:
             messagebox.showwarning("Alert","Roll number cannot be empty")
     except TypeError:
         messagebox.showwarning("Alert","Please enter correct roll number in integer")
     except ValueError:
         messagebox.showwarning("Alert","Please enter correct roll number in integer")
    
    
    


top = Tk()
L1 = Label(top, text="Enter the roll number ",).grid(row=0,column=0)
E0 = Entry(top)
E0.grid(row=0,column=1)
L=Label(top, text="",).grid(row=5,column=0)

calculate=Button(top, text ="Calculate",command = calculate).grid(row=2,column=1,)
top.title("Calculator LIC RC value")

top.mainloop()