from tkinter import *
from tkinter import ttk


class MainPageFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = ttk.Label(self, text="Добро пожаловать на главную страницу!")
        self.label.pack(pady=20)

        # Кнопка выхода
        logout_btn = ttk.Button(self, text="Выйти", command=lambda: controller.show_frame("LoginFrame"))
        logout_btn.pack(pady=10)

    def tkraise(self, *args, **kwargs):
        """Переопределяем tkraise чтобы обновить информацию при показе фрейма"""
        # Получаем данные из контроллера и обновляем интерфейс
        username = self.controller.get_shared_data("username")
        if username:
            self.label.config(text=f"Добро пожаловать, {username}!")
        super().tkraise(*args, **kwargs)