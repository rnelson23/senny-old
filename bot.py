import discord
import os
from itertools import cycle
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix=commands.when_mentioned_or('s!'))
astatus = cycle(['s!help', 'Waiting for !'])

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=35)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(astatus)))

@bot.event
async def on_ready():
    change_status.start()
    
    print(f'\nLogging in as: {bot.user.name} - {bot.user.id}\nVersion: 1.1\nDiscord: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')

bot.run('token')