import tkinter as tk
from tkinter import W


class Registration(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Регистрация", font=('Helvetica', 18, "bold"), justify="left").pack(pady=40)
        tk.Label(self, text="Введите имя",  justify="left").pack()
        name_entry=tk.Entry(self, bg='#fff', fg='#444')
        name_entry.pack()

        tk.Label(self, text="\n Введите логин", justify="left").pack()
        log_entry=tk.Entry(self, bg='#fff', fg='#444')
        log_entry.pack()

        tk.Label(self, text="\n Введите пароль", justify="left").pack()
        pass_entry=tk.Entry(self, bg='#fff', fg='#444', show="*")
        pass_entry.pack()

        tk.Label(self, text="\n Повторите пароль", justify="left").pack()
        passcorr_entry=tk.Entry(self, bg='#fff', fg='#444', show="*")
        passcorr_entry.pack()

        tk.Button(self, text="Зарегистрироваться").pack(pady=20)
        forgot_label = tk.Label(self, text='Уже зарегистрированы? Войти')
        forgot_label.bind("<Button-1>", self.signin)
        forgot_label.pack()

    def signin(self):
        pass
