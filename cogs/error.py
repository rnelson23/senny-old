import discord
import traceback
import sys
from discord.ext import commands

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, 'on_error'):
            return

        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(f'{error}')

        else:
            await ctx.send(f'{error}')

        print('\nIgnoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(error(bot))