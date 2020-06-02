import discord
from discord.ext import commands

class owner(commands.Cog, name="Owner Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def say(self, ctx, id, *, message):
        """Sends a message"""

        channel = await self.bot.fetch_channel(id)
        await channel.send(f'{message}')

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, *, msg):
        """Changes the bot status"""

        await self.bot.change_presence(activity=discord.Game((f'{msg}')))

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        """Loads a cog"""

        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'Loaded {cog}')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """Unloads a cog"""

        self.bot.unload_extension(f'cogs.{cog}')
        await ctx.send(f'Unloaded {cog}')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """Reloads a cog"""

        await ctx.send('Reloading...')
        self.bot.unload_extension(f'cogs.{cog}')
        self.bot.load_extension(f'cogs.{cog}')
        await ctx.send(f'Reloaded {cog}')

def setup(bot):
    bot.add_cog(owner(bot))