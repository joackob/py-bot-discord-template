import discord
from discord import Intents
import os


intents = Intents.all()
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Estoy logeado como {bot.user}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    mensaje = str(message.content)

    print(mensaje)

    if 'saluda' in mensaje:
        await message.channel.send('Como va gentee @everyone')

    elif 'duerme' in mensaje:
        await message.channel.send('ok....zzzzz')

    else:
        await message.channel.send('jejeje no entendi')


print(os.getenv('TOKEN'))
bot.run(os.getenv('TOKEN'))
