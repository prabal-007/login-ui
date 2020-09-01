from tkinter import *

def login_ui():
    root = Tk()
    root.title('Login UI')
    root.geometry('400x400')

    heading = Label(root,text='Login UI',font='arial 20')
    username = Label(root,text='Uer Name : ')
    entry_user = Entry(root)
    password = Label(root,text='Password : ')
    entry_pass = Entry(root)
    login_button = Button(root,text='Login',command=lambda: login(entry_user,entry_pass,msg))
    msg = Label(root)

    heading.grid(row=0, column=1,columnspan=2,pady=10)
    username.grid(row=1,column=0,padx=10)
    entry_user.grid(row=1,column=1,padx=10)
    password.grid(row=2,column=0,padx=10)
    entry_pass.grid(row=2,column=1,padx=10)
    login_button.grid(row=3,columnspan=2,pady=20)
    msg.grid(row=4,column=0)

    root.mainloop()

def login(entry_user,entry_pass,msg):
    user_name_data = 'Starkk'
    password_data = '123456789'
    if entry_user.get() == user_name_data and entry_pass.get() == password_data:
        msg.configure(text='Login Successiful')
    else:
        msg.configure(text='Login Failed')

if __name__ == "__main__":
    login_ui()
