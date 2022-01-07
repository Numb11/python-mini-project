import random,string,pyperclip
from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.title('Password Generator')
gui.geometry('250x200')
gui.resizable(0,0)

def process():
    length = int(string_pass.get())
    lower =  list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password = "".join(random.sample(lower+upper+num,length))
    messagebox.showinfo('Result', 'Your password {} \n\nPassword copied to clipboard'.format(password))
    pyperclip.copy(password)

string_pass = StringVar()
label = Label(text="Password Length").pack(pady=10)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Generate", command=process).pack(pady=10)

gui.mainloop()
