import re
import tkinter as tk

login_pattern = re.compile(r'^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$')
password_pattern = re.compile(r'^\w{8,16}$')

root = tk.Tk()
root.geometry('400x250+700+500')
root.resizable(False, False)

def logining():
	pass

login_label = tk.Label(root, text='Login', font=('Arial', 14), padx=50)
password_label = tk.Label(root, text='Password', font=('Arial', 14), padx=50)
login_entry = tk.Entry(root, font=('Arial', 12), width=20)
password_entry = tk.Entry(root, font=('Arial', 12), width=20)

root.mainloop()
