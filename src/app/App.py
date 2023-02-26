
from dataclasses import dataclass
from interfaces.interfaces import Bot, IAChat


@dataclass
class App:
    ia: IAChat
    bot: Bot

    def run(self):
        self.bot.chatWith(ia=self.ia)
