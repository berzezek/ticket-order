from channels.consumer import SyncConsumer

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    def websocket_disconnect(self, event):
        # Можно добавить любую логику, которую нужно выполнить при отключении
        print("Клиент отключился")
