import discord
from discord.ext import commands
from discord.utils import get
from discord.channel import TextChannel

class Owner(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot

#    @commands.Cog.listener()
#    async def on_command_error(self, ctx, error):

#        if isinstance(error, commands.CommandNotFound):
#            response = await ctx.send('That command does not exist!')
#            await response.delete(delay=10)

#        if isinstance(error, commands.MissingPermissions):
#            response = await ctx.send('You do not have permission to use that command!')
#            await response.delete(delay=10)

#        if isinstance(error, commands.MissingRequiredArgument):
#            response = await ctx.send('Please provide all required arguments!')
#            await response.delete(delay=10)

#        if isinstance(error, commands.NotOwner):
#            response = await ctx.send('You do not own this bot!')
#            await response.delete(delay=10)

#        if isinstance(error, commands.BadArgument):
#            response = await ctx.send('Please ensure there are no spelling errors and/or missing arguments!')
#            await response.delete(delay=10)

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, channel: discord.TextChannel, *, message):
        """Sends a message to a channel."""
        
        await channel.send(f'{message}')

    @commands.command(description='Remember to use dot path. e.g: cogs.owner')
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Loads a cog."""

        try:
            self.bot.load_extension(cog)
            await ctx.send('Loaded {}'.format(cog))

        except Exception as error:
            await ctx.send('{} cannot be loaded. [{}]'.format(cog, error))

    @commands.command(description='Remember to use dot path. e.g: cogs.owner')
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Unloads a cog."""

        try:
            self.bot.unload_extension(cog)
            await ctx.send('Unloaded {}'.format(cog))

        except Exception as error:
            await ctx.send('{} cannot be unloaded. [{}]'.format(cog, error))

    @commands.command(description='Remember to use dot path. e.g: cogs.owner')
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Reloads a cog."""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send('Reloaded {}'.format(cog))
            
        except Exception as error:
            await ctx.send('{} cannot be reloaded. [{}]'.format(cog, error))

def setup(bot):
    bot.add_cog(Owner(bot))