import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class mod(commands.Cog, name='Moderation Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        """Purges messages"""

        await ctx.channel.purge(limit=amount)
        response = await ctx.send(f'I deleted **{amount}** messages!')
        
        await response.delete(delay=10)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, name = None):
        """Changes a nickname"""

        await member.edit(nick=name)
        await ctx.send(f"I changed **{name}'s** nickname!")

    @commands.command(aliases=['gr'])
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member: discord.Member, *, role: discord.Role):
        """Gives a role"""

        await member.add_roles(role)
        await ctx.send(f'I gave **{role}** to **{member.name}**!')

    @commands.command(aliases=['rr'])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, *, role: discord.Role):
        """Removes a role"""

        await member.remove_roles(role)
        await ctx.send(f'I removed **{role}** from **{member.name}**!')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a member"""

        await member.kick(reason=reason)
        await ctx.send(f'I kicked **{member.name}**!')

    @commands.command(description='You must ping the member.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a member"""

        await member.ban(reason=reason)
        await ctx.send(f'I banned **{member.name}**!')

def setup(bot):
    bot.add_cog(mod(bot))