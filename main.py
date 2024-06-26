# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 16:07:35 2024

@author: User
"""

import tkinter
from ui import ToDoAppUI
#entry point for the ToDo application 
if __name__ == "__main__":
    #create the main window
    root = tkinter.Tk()
    # initialize the todoappUI with the root window 
    app = ToDoAppUI(root)
    #start the main event loop to make the window work 
    root.mainloop()
    
    
