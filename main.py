import discord
from discord.ext import commands
import requests
import os
import json
#import pynacl
#import dnspython
import server
updatefunc = False
bot = commands.Bot(command_prefix='!@import discord
from discord.ext import commands
import requests
import os
import json
#import pynacl
#import dnspython
import server
updatefunc = False
bot = commands.Bot(command_prefix='!p')
client = discord.Client()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def bal(ctx):
    response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'show_bal', 'author': str(ctx.author)})
    json_response = response.json()
    await ctx.send(json_response[0])
    


@bot.command()
async def select_gun(ctx):
    #Bot will say: @user select gun
    pass

@bot.command()
async def select_rifle(ctx):
    #Bot will say: @user select rifle
    pass

@bot.command()
async def select_flame(ctx):
    #Bot will say: @user select flamethrower
    await ctx.send("Working")

@bot.command()
async def select_bow(ctx):
    #Bot will say: @user select bow
    pass

@bot.command()
async def select(ctx):
    #Bot will say: The types of weapons are crossbow, gun, rifle, speaker, and flame
    pass

@bot.command()
async def shop(ctx):
    pass

async def buy(ctx, *, item):
    pass


@bot.event
async def on_message(message):
	requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file': 'money','function': 'update', 'author': str(message.author)})
	await bot.process_commands(message)

	

TOKEN = os.getenv("DISCORD_TOKEN")
server.server()
client.run(TOKEN)
client = discord.Client()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def bal(ctx):
    response = requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file':'money', 'function': 'show_bal', 'author': str(ctx.author)})
    json_response = response.json()
    await ctx.send(json_response[0])
    


@bot.command()
async def select_gun(ctx):
    #Bot will say: @user select gun
    pass

@bot.command()
async def select_rifle(ctx):
    #Bot will say: @user select rifle
    pass

@bot.command()
async def select_flame(ctx):
    #Bot will say: @user select flamethrower
    await ctx.send("Working")

@bot.command()
async def select_bow(ctx):
    #Bot will say: @user select bow
    pass

@bot.command()
async def select(ctx):
    #Bot will say: The types of weapons are crossbow, gun, rifle, speaker, and flame
    pass

@bot.command()
async def shop(ctx):
    pass

async def buy(ctx, *, item):
    pass


@bot.event
async def on_message(message):
	requests.get('https://SlobbyBot-Database.loganpollack.repl.co', params={'file': 'money','function': 'update', 'author': str(message.author)})
	await bot.process_commands(message)

	

TOKEN = os.getenv("DISCORD_TOKEN")
server.server()
client.run(TOKEN)
