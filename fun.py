import discord
import random
from discord.ext import commands

class Fun(commands.Cog, name='Fun Commands'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hug(self, ctx, member: discord.Member=None):
        """Hugs someone."""

        end = ['adorable!',
               'how cute!',
               'awww!']

        if member is None:
            await ctx.send(f'Please provide a mention/ID!')
        
        if member == ctx.author:
            await ctx.send(f'Aww does someone need a hug?')

        else:
            await ctx.send(f'***{ctx.author.name}*** *hugs* ***{member.name},*** *{random.choice(end)}*')

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        """Pats someone."""

        end = ['adorable!',
               'how cute!',
               'awww!']

        if member is None:
            await ctx.send(f'Please provide a mention/ID!')
        
        if member == ctx.author:
            await ctx.send(f'Aww does someone need to be pat?')

        else:
            await ctx.send(f'***{ctx.author.name}*** *pats* ***{member.name},*** *{random.choice(end)}*')

    @commands.command()
    async def cuddle(self, ctx, member: discord.Member):
        """Cuddles someone."""

        end = ['adorable!',
               'how cute!',
               'awww!']

        if member is None:
            await ctx.send(f'Please provide a mention/ID!')
        
        if member == ctx.author:
            await ctx.send(f'Aww does someone need to be cuddled?')

        else:
            await ctx.send(f'***{ctx.author.name}*** *cuddles* ***{member.name},*** *{random.choice(end)}*')

    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses one option."""

        try:
            await ctx.send(random.choice(choices))

        except Exception as error:
            await ctx.send(error)

    @commands.command()
    async def roll(self, ctx, dice : str):
        """Rolls a dice in NdN format."""

        try:
            rolls, limit = map(int, dice.split('d'))

        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        
        await ctx.send(result)

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        """Provides wisdom."""

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

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """Adds two integer values."""

        total = first + second

        await ctx.send(f'The sum of **{first}** and **{second}** is **{total}**')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello."""

        member = member or ctx.author

        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))

        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))

        self._last_member = member

    @commands.command(aliases=['thanks', 'thank you', 'Thank you', 'Thank', 'Thanks'], hidden=True)
    async def thank(self, ctx):

        response = [f"You're welcome!",
                    f'No problem!',
                    f'My pleasure!',
                    f'Glad I could help!',
                    f"That's what I'm here for!"]

        await ctx.send(random.choice(response))

    @commands.command(aliases=['Danke'], hidden=True)
    async def danke(self, ctx):
        
        await ctx.send(f'Bitte!')

def setup(bot):
    bot.add_cog(Fun(bot))