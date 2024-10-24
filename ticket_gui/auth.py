import asyncio
from tkinter import *
from tkinter import ttk

from client import WebSocketClient

class Session:
    def __init__(self):
        self.token = None
        self.is_superuser = False

    def login(self, token):
        self.token = token

    def logout(self):
        self.token = None



# Фрейм для авторизации
class LoginFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        login_label = ttk.Label(self, text="Авторизация")
        login_label.pack(pady=10)

        login_name_label = ttk.Label(self, text="Введите имя")
        login_name_label.pack(anchor=NW, padx=10)

        self.login_name_entry = ttk.Entry(self)
        self.login_name_entry.pack(anchor=NW, padx=10)

        login_pass_label = ttk.Label(self, text="Введите пароль")
        login_pass_label.pack(anchor=NW, padx=10)

        self.login_pass_entry = ttk.Entry(self, show="*")
        self.login_pass_entry.pack(anchor=NW, padx=10)

        btn_login = ttk.Button(self, text="Войти", command=self.login)
        btn_login.pack(pady=10)

        # Кнопка для переключения на фрейм регистрации
        to_register_btn = ttk.Button(self, text="Нет аккаунта? Регистрация", command=lambda: controller.show_frame("RegisterFrame"))
        to_register_btn.pack(pady=5)

    def login(self):
        username = self.login_name_entry.get()
        password = self.login_pass_entry.get()

        if username and password:
            self.controller.set_shared_data("username", username)

            # Создаем клиент и запускаем асинхронные задачи
            client = WebSocketClient("ws://127.0.0.1:8001/ws/chat/")
            self.controller.run_async(self.connect_and_send(client, username))

            # Переключаемся на главную страницу
            self.controller.show_frame("MainPageFrame")
        else:
            print("Ошибка: Имя пользователя и пароль не должны быть пустыми")


    async def connect_and_send(self, client, username):
        """Асинхронная задача для подключения и отправки сообщения"""
        await client.connect()
        await client.send_message(username)
        await client.close()

# Фрейм для регистрации (остался без изменений)
class RegisterFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        register_label = ttk.Label(self, text="Регистрация")
        register_label.pack(pady=10)

        register_name_label = ttk.Label(self, text="Введите имя")
        register_name_label.pack(anchor=NW, padx=10)

        register_name_entry = ttk.Entry(self)
        register_name_entry.pack(anchor=NW, padx=10)

        register_email_label = ttk.Label(self, text="Введите Email")
        register_email_label.pack(anchor=NW, padx=10)

        register_email_entry = ttk.Entry(self)
        register_email_entry.pack(anchor=NW, padx=10)

        register_pass_label = ttk.Label(self, text="Введите пароль")
        register_pass_label.pack(anchor=NW, padx=10)

        register_pass_entry = ttk.Entry(self, show="*")
        register_pass_entry.pack(anchor=NW, padx=10)

        btn_register = ttk.Button(self, text="Зарегистрироваться", command=lambda: print("Регистрация"))
        btn_register.pack(pady=10)

        # Кнопка для переключения на фрейм авторизации
        to_login_btn = ttk.Button(self, text="Уже есть аккаунт? Войти", command=lambda: controller.show_frame("LoginFrame"))
        to_login_btn.pack(pady=5)