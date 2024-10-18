from tkinter import *
from backend import Hospital
from db_prep import prepare_db

root = Tk()
root.title("Hospital Management System - 2024")
root.geometry('500x500')
lbl = Label(root, text = "Manage your hospital database efficiently with HMS.")
lbl.grid()
root.mainloop()