import asyncio
import requests
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LiveDashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.update_task = asyncio.create_task(self.send_updates())
        await self.accept()

    async def disconnect(self, close_code):
        self.update_task.cancel()

    async def send_updates(self):
        try:
            while True:
                try:
                    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
                    response.raise_for_status()
                    data = response.json()
                    await self.send(json.dumps({'price': data['bitcoin']['usd']}))
                except requests.RequestException as e:
                    print(f"Error fetching data: {e}")
                    await asyncio.sleep(10)
                    continue
                await asyncio.sleep(10)
        except asyncio.CancelledError:
            pass