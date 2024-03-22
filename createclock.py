#!/usr/bin/python3
# -*- Digital Clock -*-
"""
Created on Fri March 22 2024
@author: Okeke Morgan
"""
from tkinter import Tk
from tkinter import Label
import time
import sys

if __name__ == '__main__':
    master = Tk()
    master.title("Digital Clock")

    def get_time():
        """
            Return:
                None
        """
        timeVar = time.strftime("%H:%M:%S %p %A")
        clock.config(text=timeVar)
        clock.after(200,get_time)


    clock = Label(master, font=("Calibri",90),bg="grey",fg="white")
    clock.pack()

    get_time()

    master.mainloop()
