from os import getenv
from app.App import App
from bot.DiscordBot import DiscordBot
from gpt.GPTIA import GPTIA


def main():
    ia = GPTIA(tokenChatGPTSession=getenv('TOKEN_GPT_SESSION'))
    bot = DiscordBot(tokenBotDiscord=getenv('TOKEN_BOT_DISCORD'),
                     iaToChat=ia)
    app = App(bot=bot, ia=ia)
    app.run()


if __name__ == '__main__':
    main()
