from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import random
from spacexapi import *
import time


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='sx ')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    print(len(bot.guilds))


bot.run(TOKEN)
bot.logout()
