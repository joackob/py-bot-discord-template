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
    autor = str(message.author)

    print(f'Escuche el mensaje: "{mensaje}" de {autor}')

    if 'saluda' in mensaje:
        await message.channel.send('Como va gentee @everyone')

    elif 'duerme' in mensaje:
        await message.channel.send('ok....zzzzz')
        await bot.close()

    else:
        await message.channel.send('jejeje no entendi')


bot.run(os.getenv('TOKEN'))
