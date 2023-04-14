# импортируем библиотеку tkinter всю сразу
import tkinter
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        font_header = ('Arial', 15)
        font_entry = ('Arial', 12)
        label_font = ('Arial', 11)
        base_padding = {'padx': 10, 'pady': 8}
        header_padding = {'padx': 10, 'pady': 30}

        main_label = tk.Label(self, text='Авторизация', font=('Helvetica', 18, "bold"), **header_padding)
        # помещаем виджет в окно по принципу один виджет под другим
        main_label.pack()

        # метка для поля ввода имени
        username_label = tk.Label(self, text='Имя пользователя', font=label_font, **base_padding)
        username_label.pack()

        # поле ввода имени
        username_entry = tk.Entry(self, bg='#fff', fg='#444', font=font_entry)
        username_entry.pack()

        # метка для поля ввода пароля
        password_label = tk.Label(self, text='Пароль', font=label_font, **base_padding)
        password_label.pack()

        # поле ввода пароля
        password_entry = ttkbootstrap.Entry(self, font=font_entry, show="*")
        password_entry.pack()

        # кнопка отправки формы
        send_btn = tk.Button(self, text='Войти', command=self.clicked)
        send_btn.pack(**base_padding)

        forgot_label = tk.Label(self, text='Забыли пароль?', font=label_font, **base_padding)
        forgot_label.bind("<Button-1>", self.forgot)
        forgot_label.pack()

        image = tk.PhotoImage(file="D:\Materials\Дипломная работа\Materials\doc.png")

        label = tk.Label(self, image=image)
        label.pack()

        # обработчик нажатия на клавишу 'Войти'
    def clicked(self):
        pass

    def forgot(self):
        pass
