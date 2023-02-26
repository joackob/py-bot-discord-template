from dataclasses import dataclass
from discord import Client, Intents, Message
from interfaces.interfaces import Bot, IAChat


class FakeIAChat(IAChat):
    def chat(self, message: str) -> str:
        return f'No puedo responder a "{message}"'


@dataclass
class DiscordBot(Bot, Client):

    def __init__(self, tokenBotDiscord: str, iaToChat: IAChat = FakeIAChat()):
        Client.__init__(self, intents=Intents.all())
        self.ia = iaToChat
        self.run(token=tokenBotDiscord)

    def chatWith(self, ia: IAChat) -> None:
        self.ia = ia

    async def on_ready(self):
        print(f"Estoy logeado como {self.user}")

    async def on_message(self, message: Message):
        if message.author == self.user:
            return

        print(f'Escuche el mensaje: "{message.content}" de {message.author}')

        if 'duerme' in message.content:
            await message.channel.send('ok....zzzzz')
            await self.close()
        else:
            response = self.ia.chat(message=message.content)
            await message.channel.send(content=response)
