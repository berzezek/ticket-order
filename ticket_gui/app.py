import asyncio
from tkinter import *
from tkinter import ttk

from auth import LoginFrame, RegisterFrame
from main import MainPageFrame
from mixins import DataMixins

frame_list = [LoginFrame, RegisterFrame, MainPageFrame]

# Класс для запуска асинхронных задач в Tkinter
class AsyncTk(Tk, DataMixins):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ticket Order")
        self.geometry("300x250")
        self.shared_data = {}

        # Создаем контейнер для фреймов
        self.container = Frame(self)
        self.container.pack(fill=Y, expand=True)

        # Словарь для хранения всех фреймов
        self.frames = {}
        self.loop = asyncio.new_event_loop()  # Обновлено
        asyncio.set_event_loop(self.loop)     # Обновлено
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        for F in frame_list:
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

    def show_frame(self, frame_name):
        """Показывает фрейм по имени класса"""
        frame = self.frames[frame_name]
        frame.tkraise()

    def run_async(self, coro):
        """Метод для запуска асинхронной задачи"""
        self.loop.create_task(coro)

    def on_close(self):
        self.loop.stop()
        self.destroy()

if __name__ == "__main__":
    app = AsyncTk()
    app.mainloop()
