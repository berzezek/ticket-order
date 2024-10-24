import asyncio
import websockets
import json

class WebSocketClient:
    def __init__(self, uri):
        self.uri = uri
        self.websocket = None

    async def connect(self):
        """Устанавливаем соединение с сервером"""
        self.websocket = await websockets.connect(self.uri)
        print("Подключение к серверу установлено. Вы можете отправлять сообщения.")

        # Запускаем задачу для прослушивания сообщений от сервера
        asyncio.create_task(self.receive_messages())

    async def send_message(self, text):
        """Отправляем сообщение на сервер"""
        if self.websocket:
            await self.websocket.send(json.dumps({"message": text}))
            print(f"Сообщение отправлено: {text}")
        else:
            print("Соединение не установлено. Пожалуйста, подключитесь к серверу.")

    async def receive_messages(self):
        """Функция для получения сообщений от сервера"""
        try:
            async for response in self.websocket:
                data = json.loads(response)
                print(f"Ответ от сервера: {data.get('message')}")
        except websockets.ConnectionClosed:
            print("Соединение с сервером закрыто.")

    async def close(self):
        """Закрываем соединение с сервером"""
        if self.websocket:
            await self.websocket.close()
            print("Соединение закрыто.")

# Пример использования WebSocketClient
async def main():
    client = WebSocketClient("ws://127.0.0.1:8001/ws/chat/")
    await client.connect()

    # Отправляем сообщения в любое время
    await client.send_message("Первое сообщение")
    await asyncio.sleep(2)
    await client.send_message("Второе сообщение")

    # Дождитесь некоторых событий перед закрытием
    await asyncio.sleep(5)
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
