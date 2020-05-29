import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class Mod(commands.Cog, name='Moderation Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['clear'], description='The command is counted towards the number of messages deleted.')
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=1):
        """Deletes x amount of messages."""

        log_channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed=discord.Embed()

        embed.set_author(name='Bulk Messages Deleted')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Count', value=f'{amount}')

        await ctx.channel.purge(limit=amount)
        await log_channel.send(embed=embed)
        response = await ctx.send(f'I deleted **{amount}** messages!')
        
        await response.delete(delay=10)

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: discord.Member, *, name = None):
        """Changes a member's nickname."""

        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Nickname Changed')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Member', value=f'{member.mention} {member}')
        embed.add_field(name='New Nickname', value=f'{name}')

        await member.edit(nick=name)
        await ctx.send(f"I changed **{member.name}'s** nickname to **{name}**!")
        await channel.send(embed=embed)

    @commands.command(aliases=['gr'])
    @commands.has_permissions(manage_roles=True)
    async def giverole(self, ctx, member: discord.Member, *, role: discord.Role):
        """Gives a member a role."""

        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Role Given')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Member', value=f'{member.mention} {member}')
        embed.add_field(name='Role', value=f'{role.mention}')

        await member.add_roles(role)
        await ctx.send(f'I gave the role **{role}** to **{member.name}** !')
        await channel.send(embed=embed)

    @commands.command(aliases=['rr'])
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: discord.Member, *, role: discord.Role):
        """Removes a role from a member."""

        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Role Removed')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Member', value=f'{member.mention} {member}')
        embed.add_field(name='Role', value=f'{role.mention}')

        await member.remove_roles(role)
        await ctx.send(f'I took the role **{role}** from **{member.name}**!')
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Gives someone the mute role."""

        role = discord.utils.get(ctx.guild.roles, name='Muted')
        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Member Muted')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='User', value=f'{member.mention} {member}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.add_roles(role)
        await ctx.send(f'I muted **{member.name}**!')
        await channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """Removes the muted role from someone."""

        role = discord.utils.get(ctx.guild.roles, name='Muted')
        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Member Unmuted')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='User', value=f'{member.mention} {member}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.remove_roles(role)
        await ctx.send(f'I unmuted **{member.name}**!')
        await channel.send(embed=embed)

    @commands.command(description='You must ping the member.')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a member."""
        
        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Member Kicked')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Member', value=f'{member.mention} {member}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.kick(reason=reason)
        await ctx.send(f'I kicked **{member.name}**!')
        await channel.send(embed=embed)

    @commands.command(description='You must ping the member.')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a member."""

        channel = discord.utils.get(ctx.guild.text_channels, name='senny-logs')
        embed = discord.Embed()

        embed.set_author(name='Member Banned')
        embed.add_field(name='Moderator', value=f'{ctx.author.mention}')
        embed.add_field(name='Member', value=f'{member.mention} {member}')
        embed.add_field(name='Reason', value=f'{reason}')

        await member.ban(reason=reason)
        await ctx.send(f'I banned **{member.name}**!')
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Mod(bot))