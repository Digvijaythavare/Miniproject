import tkinter as tk
from tkinter import messagebox
def login():
     username = entry_user.get() # type: ignore
     password = entry_pass.get() # type: ignore
     if username == "user" and password == "1234": 
       messagebox.showinfo("Login Success","Wlcome Admin")
     else:
         messagebox.showinfo("Login Failed")
root = tk.Tk()
root.title("Login Form")
root.geometry(300*200)

lable_user = tk.Label(root,text="Username")
lable_user.pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack(pady=5)    

lable_pass = tk.Label(root,text="Password")
lable_pass.pack(pady=5)
entry_pass = tk.Entry(root,show="*")
entry_pass.pack(pady=5)         

btn_login = tk.Button(root, text="Login",
    command=login)
btn_login.pack(pady=5)

root.mainloop()