import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        await self.send(text_data=json.dumps({
            'message': 'Hello from Django socket!'
        }))

    async def disconnect(self, close_code):
        pass
