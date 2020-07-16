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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("sx help. Connected to " + str(len(bot.guilds)) + " servers."))
    print("Bot is Ready")


@ bot.command(name='next')
async def nine_nine(ctx):
    await ctx.send(next_launch())


@ bot.command(name='previous')
async def nine_nine(ctx):
    embed = discord.Embed()
    embed.set_image(
        url=image())

    await ctx.send(embed=embed)
    await ctx.send(previous_launch())


@ bot.command(name='launch')
async def nine_nine(ctx):
    embed = discord.Embed(
        title="SpaceX Goes Brrrrrr!!!!!"
    )
    embed.set_image(
        url=launch_image())
    await ctx.send(embed=embed)


@ bot.command(name='image')
async def displayemded(ctx):
    embed = discord.Embed()
    embed.set_image(
        url=random_gif())

    await ctx.send(embed=embed)


@ bot.command(name='nasa')
async def displayemded(ctx):
    embed = discord.Embed()
    embed.set_image(
        url='https://www.youtube.com/watch?v=21X5lGlDOfg')

    await ctx.send('https://www.youtube.com/watch?v=21X5lGlDOfg')


@ bot.command(name='isro')
async def displayemded(ctx):
    embed = discord.Embed()
    embed.set_image(
        url=isro())

    await ctx.send(embed=embed)


@ bot.command(name='server')
async def nine_nine(ctx):
    await ctx.send("Deployed and running on " + str(len(bot.guilds)) + " servers.")

bot.run(TOKEN)
