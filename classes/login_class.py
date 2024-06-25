import customtkinter as ctk
import tkinter.messagebox as tkmb


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login to start')
        self.root.geometry('300x300')

        self.username = 'Damian'
        self.password = 'tajne'

        self.user_label = ctk.CTkLabel(root, text='Username')
        self.user_label.pack(pady=5)
        self.user_entry = ctk.CTkEntry(root)
        self.user_entry.pack(pady=5)

        self.pass_label = ctk.CTkLabel(root, text='Password')
        self.pass_label.pack(pady=5)
        self.user_pass = ctk.CTkEntry(root, show='')
        self.user_pass.pack(pady=5)

        self.login_button = ctk.CTkButton(root, text='Login', command=self.login_user)
        self.login_button.pack(pady=20)

    def login_user(self):
        user_entry = self.user_entry.get()
        user_pass = self.user_pass.get()

        # new_window = ctk.CTkToplevel(self.root)
        # new_window.title('Login')
        # new_window.geometry('350x150')

        if user_entry == self.username and user_pass == self.password:
            tkmb.showinfo(title='Login Successful', message='You have logged in Successfully')
            # ctk.CTkLabel(new_window, text='').pack()

        elif user_entry == self.username and user_pass != self.password:
            tkmb.showwarning(title='Wrong password', message='Please check your password')

        elif user_entry != self.username and user_pass == self.password:
            tkmb.showwarning(title='Wrong username', message='Please check your username')

        else:
            tkmb.showerror(title='Login Failed', message='Invalid Username and password')
