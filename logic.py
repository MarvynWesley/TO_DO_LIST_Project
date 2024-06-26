# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:20:04 2024

@author: User
"""

import random
# the ToDoApLogic class contains the logic and functionality of the ToDo application
class ToDoAppLogic:
    def __init__(self):
        #initialize the task list and the set of completed tasks 
        self.tasks = []
        self.completed_tasks = set()
    
    def add_task(self):
        # Add a task to the task list 
        task = self.txt_input.get()
        if task != '':
            self.tasks.append(task)
            self.update_listbox()
            self.display['text'] = "Task added!"
        else:
            self.display['text'] = "Please enter a task!"
            #clear the input field after adding the task 
        self.txt_input.delete(0, 'end')
    
    def delete(self):
        #deleted the task that is selected from the task list 
        selected_task = self.lb_tasks.get('active')
        if selected_task in self.tasks:
            self.tasks.remove(selected_task)
            self.update_listbox()
            self.display['text'] = "Task deleted!"
    
    def delete_all(self):
        #delete all tasks 
        self.tasks = []
        self.update_listbox()
        self.display['text'] = "All tasks deleted!"
    
    def choose_random(self):
        #choose a random task from the list and dislpay it 
        if self.tasks:
            random_task = random.choice(self.tasks)
            self.display['text'] = random_task
        else:
            self.display['text'] = "No tasks to choose from!"
    
    def number_of_task(self):
        #display the number of tasks in the list 
        count = len(self.tasks)
        self.display['text'] = f"Number of tasks: {count}"
    
    def mark_complete(self):
        #mark the selected task that it is complete 
        selected_task = self.lb_tasks.get('active')
        if selected_task in self.tasks:
            self.completed_tasks.add(selected_task)
            self.update_listbox()
            self.display['text'] = "Task is completed"

