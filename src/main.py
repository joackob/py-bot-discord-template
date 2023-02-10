import discord
from discord import Intents
from discord import Message
import os


intents = Intents.all()
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Estoy logeado como {bot.user}")


@bot.event
async def on_message(message: Message):
    if message.author == bot.user:
        return

    mensaje = message.content
    autor = message.author

    print(f'Escuche el mensaje: "{mensaje}" de {autor}')

    if 'saluda' in mensaje:
        await message.channel.send('Como va gentee @everyone')
    elif 'duerme' in mensaje:
        await message.channel.send('ok....zzzzz')
        await bot.close()
    elif 'comandos' in mensaje:
        await message.channel.send('Por el momento solo puedo saludar con "saluda" y dormir con "duerme"')
    else:
        await message.channel.send('jejeje no entendi')


bot.run(os.getenv('TOKEN'))
