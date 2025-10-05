from tkinter import messagebox
from interface import newWindow

def validate_login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()

    

    if userid == "goat" and password == "password":
        newWindow()
    else:
        messagebox.showinfo("Login Failed, Try Again.")
        

        

    
    
        





