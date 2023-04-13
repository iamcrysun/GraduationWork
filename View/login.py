# импортируем библиотеку tkinter всю сразу
from tkinter import *
from tkinter import messagebox
import ttkbootstrap
from PIL import ImageTk

# главное окно приложения
window = ttkbootstrap.Window(themename="darkly")
# заголовок окна
window.title('Авторизация')
# размер окна
window.geometry('900x600')
# можно ли изменять размер окна - нет
window.resizable(False, False)

frame_auth = Frame(window)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 30}


# обработчик нажатия на клавишу 'Войти'
def clicked():

    # получаем имя пользователя и пароль
    username = username_entry.get()
    password = password_entry.get()

    # выводим в диалоговое окно введенные пользователем данные
    messagebox.showinfo('Заголовок', '{username}, {password}'.format(username=username, password=password))

def forgot():
    pass


# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(frame_auth, text='Авторизация', font=font_header, justify=CENTER, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

# метка для поля ввода имени
username_label = Label(frame_auth, text='Имя пользователя', font=label_font , **base_padding)
username_label.pack()

# поле ввода имени
username_entry = Entry(frame_auth, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

# метка для поля ввода пароля
password_label = Label(frame_auth, text='Пароль', font=label_font , **base_padding)
password_label.pack()

# поле ввода пароля
password_entry = ttkbootstrap.Entry(frame_auth,  font=font_entry, show="*")
password_entry.pack()

# кнопка отправки формы
send_btn = Button(frame_auth, text='Войти', command=clicked)
send_btn.pack(**base_padding)

forgot_label = Label(frame_auth, text='Забыли пароль?', font=label_font,  **base_padding)
forgot_label.bind("<Button-1>", forgot)
forgot_label.pack()

image = PhotoImage(file="D:\Materials\Дипломная работа\Materials\doc.png")

label = Label(frame_auth, image = image)
label.pack()
# запускаем главный цикл окна
frame_auth.pack()
window.mainloop()