import tkinter as tk
from tkinter.ttk import *
import entry

def Window(master_window):
    
    #Config for Window
    LoginFrame= tk.Toplevel(master_window)
    LoginFrame.geometry('700x400')
    LoginFrame.title("Login")

    #Setting Username buttons
    username_label = tk.Label(LoginFrame, text="Userid:")
    username_label.pack()
    username_entry = tk.Entry(LoginFrame)
    username_entry.pack()

    #Setting Password Buttons
    password_label = tk.Label(LoginFrame, text= "Password:")
    password_label.pack()
    #Cover User Input with *
    password_entry = tk.Entry(LoginFrame, show="*")
    password_entry.pack()


    #Setting LoginFrame button and Parameters
    login_button = tk.Button(LoginFrame, text="Login", 
                             command=lambda: entry.validate_login(username_entry, password_entry))
    login_button.pack()

    #Setting Quit Button to Exit Programm
    quit_button = tk.Button(LoginFrame, text = "Quit", command=LoginFrame.destroy)
    quit_button.place(x=330, y=125)
    
    #Loop to Keep Window open
    LoginFrame.mainloop()   
    
    #Still in Progress (Vault Window)
def VaultFrame(LoginFrame):
    vault = tk.Toplevel(LoginFrame)
    vault.title("Vault")
    vault.geometry('700x400')
    
def MasterFrame():
    master_window = tk.Tk()
    master_window.title("Master Login")
    master_window.geometry('700x400')

    masterkey_label = tk.Label(master_window, text="Master Key")
    masterkey_label.pack()
    masterkey_entry = tk.Entry(master_window)
    masterkey_entry.pack()
    
    def OnLogin():
        if entry.master_login(masterkey_entry, master_window):
            Login_Master['state'] = 'disabled'
            Window(master_window)
            master_window.destroy()
    
      
    Login_Master = tk.Button(master_window, text ="Login", command=OnLogin)
    Login_Master.pack()
    
    master_window.mainloop()
    
