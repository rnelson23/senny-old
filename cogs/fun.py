import discord
import random
from discord.ext import commands

class Fun(commands.Cog, name='Fun Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses an option"""

        await ctx.send(random.choice(choices))

    @commands.command()
    async def roll(self, ctx, dice : str):
        """Rolls a dice"""

        rolls, limit = map(int, dice.split('d'))
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        
        await ctx.send(result)

    @commands.command(name='8ball')
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        """Provides wisdom"""

        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes - definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(Fun(bot))