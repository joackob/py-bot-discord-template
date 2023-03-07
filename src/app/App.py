
from dataclasses import dataclass
from interfaces.interfaces import Bot, IAChat


@dataclass
class App:
    ia: IAChat
    bot: Bot

    def run(self):
        self.ia.run()
        self.bot.run()
        return self

    def setup(self):
        self.bot.event_chat = self.chat_with_ia
        return self

    async def chat_with_ia(self):
        query = await self.bot.get_query()
        response = await self.ia.chat(query=query)
        await self.bot.send_response(response=response)
        return self
