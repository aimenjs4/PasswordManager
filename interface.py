import tkinter as tk
from tkinter.ttk import *
import entry

def Window():
    
    window = tk.Tk()
    window.geometry('700x400')
    window.title("miner")


    username_label = tk.Label(window, text="Userid:")
    username_label.pack()

    username_entry = tk.Entry(window)
    username_entry.pack()


    password_label = tk.Label(window, text= "Password:")
    password_label.pack()

    password_entry = tk.Entry(window, show="*")
    password_entry.pack()



    login_button = tk.Button(window, text="Login", 
                             command=lambda: entry.validate_login(username_entry, password_entry))
    login_button.pack()

    quit_button = tk.Button(window, text = "Quit", command=window.destroy)
    quit_button.place(x=330, y=125)
    
    window.mainloop()   
    
def newWindow(window):
    vault = tk.Toplevel(window)
    vault.title("Vault")
    vault.ge