import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or('s?'))

cogs = ['cogs.fun',
        'cogs.mod',
        'cogs.admin',
        'cogs.owner',
        'cogs.error',
        'cogs.utility']

@bot.event
async def on_ready():
    game = discord.Game("s?help")
    await bot.change_presence(activity=game)
    
    print(f'{bot.user.name} is ready!')

    for cog in cogs:
        bot.load_extension(cog)

    return

bot.run('NjgxODY4MzYyNTk0MTIzODA2.XmpF7Q.eFGbPRPenQf3rRQk_Zi6eCe57yc')