import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap

from View.login import Login
from View.registration import  Registration

# главное окно приложения


window = ttkbootstrap.Window(themename="darkly")
# заголовок окна
window.title('Проверка трафика')
# размер окна
window.geometry('900x600')
# можно ли изменять размер окна - нет
window.resizable(False, False)

reg=Registration(window)
reg.pack()
window.mainloop()

