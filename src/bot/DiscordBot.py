from dataclasses import dataclass
from discord import Client, Intents, Message
from interfaces.interfaces import Bot


@dataclass
class DiscordBot(Bot, Client):
    def __init__(self, tokenBotDiscord: str):
        Client.__init__(self, intents=Intents.all())
        Bot.__init__(self)
        self.token: str = tokenBotDiscord
        self.last_message: Message = None

    def run(self):
        Client.run(self, token=self.token)

    async def get_query(self) -> str:
        return self.last_message.content

    async def send_response(self, response: str) -> None:
        await self.last_message.channel.send(content=response)

    async def on_ready(self):
        print(f"Estoy logeado como {self.user}")

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        self.last_message = message

        if 'duerme' in message.content:
            await message.channel.send('ok....zzzzz')
            await self.close()
        else:
            await self._handle_chat()
