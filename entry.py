from tkinter import messagebox
import interface


def validate_login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()

    

    if userid == "goat" and password == "password":
        messagebox.showinfo("Welcome Back")
    else:
        messagebox.showinfo("Login Failed, Try Again.")
        
def master_login(masterkey_entry, master_window):
    masterid = masterkey_entry.get()
    
    if masterid == "aimen":
        interface.Window(master_window)
        return True
        
    else:
        messagebox.showinfo("Wrong Master Key try again")
        return False
        

    
        

    
    
        





