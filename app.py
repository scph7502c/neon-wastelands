import customtkinter as ctk
from classes.login_class import Login

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == '__main__':
    app = ctk.CTk()
    app.geometry('400x400')
    app.title('Neon Wastelands')
    Login(app)
    app.mainloop()
