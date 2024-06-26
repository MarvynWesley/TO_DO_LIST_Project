# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:21:51 2024

@author: User
"""

import tkinter
from logic import ToDoAppLogic
#the ToDoAppUI class is in charge of the GUI for the ToDO application 
class ToDoAppUI(ToDoAppLogic):
    def __init__(self, root):
        #initialize the logic part of the application 
        super().__init__()
        #configure the window 
        self.root = root
        self.root.configure(bg='purple')
        self.root.title('My To Do List')
        self.root.geometry('800x600')
        #initialize the UI 
        self.init_ui_components()
    
    def init_ui_components(self):
        #create title and placing 
        self.title = tkinter.Label(self.root, text="To-Do-List", bg='purple', font=("Times New Roman", 12, 'bold'))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)
        #customing the windows interface 
        self.display = tkinter.Label(self.root, text="", bg='purple')
        self.display.grid(row=1, column=0, columnspan=10, pady=10)
        #creating frame of widgets 
        input_frame = tkinter.Frame(self.root, bg='black')
        input_frame.grid(row=2, column=0, padx=10, pady=10)
        #creatting frame of the listbox 
        listbox_frame = tkinter.Frame(self.root, bg='black')
        listbox_frame.grid(row=2, column=1, rowspan=8, padx=10, pady=10)
        #creating the the task input widget 
        self.txt_input = tkinter.Entry(input_frame, width=40)
        self.txt_input.grid(row=0, column=1, padx=10, pady=10)
        self.txt_input.bind("<Return>", lambda event: self.add_task())
        #create the buttons 
        self.create_buttons(input_frame)
        #create the listbox to display tasks 
        self.lb_tasks = tkinter.Listbox(listbox_frame, width=40, height=20)
        self.lb_tasks.grid(row=0, column=0, padx=10, pady=10)
        self.lb_tasks.bind("<Double-Button-1>", lambda event: self.delete())
    
    def create_buttons(self, input_frame):
        #define the font for the buttons 
        button_font = ("Times New Roman", 12, "bold")
        #task button 
        self.btn_add_task = tkinter.Button(input_frame, text="Add Task", width=10, command=self.add_task, font=button_font)
        self.btn_add_task.grid(row=0, column=0, padx=10, pady=10)
        #delete button
        self.btn_delete = tkinter.Button(input_frame, text="Delete", width=20, command=self.delete, font=button_font)
        self.btn_delete.grid(row=1, column=0, padx=10, pady=10)
        #Delete all button 
        self.btn_delete_all = tkinter.Button(input_frame, text="Delete All", width=10, command=self.delete_all, font=button_font)
        self.btn_delete_all.grid(row=2, column=0, padx=10, pady=10)
        #choose random button 
        self.btn_choose_random = tkinter.Button(input_frame, text="Choose Random", width=20, command=self.choose_random, font=button_font)
        self.btn_choose_random.grid(row=3, column=0, padx=10, pady=10)
        #number of tasks button
        self.btn_number_of_tasks = tkinter.Button(input_frame, text="Number of Tasks", width=12, command=self.number_of_task, font=button_font)
        self.btn_number_of_tasks.grid(row=4, column=0, padx=10, pady=10)
        #mark ocmplete button 
        self.btn_mark_complete = tkinter.Button(input_frame, text="Task Complete", width=20, command=self.mark_complete, font=button_font)
        self.btn_mark_complete.grid(row=5, column=0, padx=10, pady=10)
        #exit buttton 
        self.btn_exit = tkinter.Button(input_frame, text="Exit", width=10, command=self.exit, font=button_font)
        self.btn_exit.grid(row=6, column=0, padx=10, pady=10)
    
    def exit(self):
        #destroy the root window to exit 
        self.root.destroy()

    def update_listbox(self):
        #update the listbox to display current tasks 
        self.lb_tasks.delete(0, 'end')
        for idx, task in enumerate(self.tasks):
            self.lb_tasks.insert('end', task)
            #highlight the completed tasks 
            if task in self.completed_tasks:
                self.lb_tasks.itemconfig(idx, {'bg': 'black', 'fg': 'green'})
