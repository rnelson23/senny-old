import discord
from discord.ext import commands

class Admin(commands.Cog, name='Administration Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def icon(self, ctx, icon):

        await ctx.guild.edit(icon=icon)

    @commands.command(aliases=['cr'])
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, *, name):
        """Creates a role."""

        await ctx.guild.create_role(name=name)
        await ctx.send(f'I have created the role **{name}!**')

    @commands.command(aliases=['dr'])
    @commands.has_permissions(manage_roles=True)
    async def deleterole(self, ctx, role: discord.Role):
        """Deletes a role."""

        await role.delete()
        await ctx.send(f'I have deleted the role **{role.name}!**')

    @commands.command(aliases=['ern'])
    @commands.has_permissions(manage_roles=True)
    async def editrolename(self, ctx, role: discord.Role, *, name):
        """Edits a role name."""

        await role.edit(name=name)
        await ctx.send(f"I have edited the role {role.mention}'s name!")

    @commands.command(aliases=['erc'])
    @commands.has_permissions(manage_roles=True)
    async def editrolecolor(self, ctx, role: discord.Role, color: discord.Color):
        """Edits a role color."""

        await role.edit(color=color)
        await ctx.send(f"I have edited the role {role.mention}'s color!")

    @commands.command(aliases=['ct'])
    @commands.has_permissions(manage_channels=True)
    async def createtext(self, ctx, *, channel):
        """Creates a text channel."""

        await ctx.guild.create_text_channel(name=channel)
        await ctx.send(f'I have created the text channel {channel.mention}!')

    @commands.command(aliases=['cv'])
    @commands.has_permissions(manage_channels=True)
    async def createvoice(self, ctx, *, channel):
        """Creates a voice channel."""

        await ctx.guild.create_voice_channel(name=channel)
        await ctx.send(f'I have created the voice channel {channel.mention}!')

    @commands.command(aliases=['cc'])
    @commands.has_permissions(manage_channels=True)
    async def createcategory(self, ctx, *, channel):
        """Creates a category."""

        await ctx.guild.create_category_channel(name=channel)
        await ctx.send(f'I have created the category {channel.mention}!')

    @commands.command(aliases=['etn'])
    @commands.has_permissions(manage_channels=True)
    async def edittextname(self, ctx, channel: discord.TextChannel, *, name):
        """Edits a text channel name."""

        await channel.edit(name=name)
        await ctx.send(f"I have edited the text channel {channel.mention}'s name!")

    @commands.command(aliases=['evn'])
    @commands.has_permissions(manage_channels=True)
    async def editvoicename(self, ctx, channel: discord.VoiceChannel, *, name):
        """Edits a voice channel name."""

        await channel.edit(name=name)
        await ctx.send(f"I have edited the voice channel {channel.mention}'s name!")

    @commands.command(aliases=['ecn'])
    @commands.has_permissions(manage_channels=True)
    async def editcategoryname(self, ctx, channel: discord.CategoryChannel, *, name):
        """Edits a category name."""

        await channel.edit(name=name)
        await ctx.send(f"I have edited the category {channel.mention}'s name!")

    @commands.command(aliases=['mt'])
    @commands.has_permissions(manage_channels=True)
    async def movetext(self, ctx, channel: discord.TextChannel, *, category: discord.CategoryChannel):
        """Moves a text channel to a category."""

        await channel.edit(category=category)
        await ctx.send(f'I have moved the text channel {channel.mention} to the category {category.mention}!')

    @commands.command(aliases=['mv'])
    @commands.has_permissions(manage_channels=True)
    async def movevoice(self, ctx, channel: discord.VoiceChannel, *, category: discord.CategoryChannel):
        """Moves a voice channel to a category."""

        await channel.edit(category=category)
        await ctx.send(f'I have moved the voice channel {channel.mention} to the category {category.mention}!')

    @commands.command(aliases=['dt'])
    @commands.has_permissions(manage_channels=True)
    async def deletetext(self, ctx, channel: discord.TextChannel, *, reason=None):
        """Deletes a text channel."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I have deleted the text channel **{channel}!**')

    @commands.command(aliases=['dv'])
    @commands.has_permissions(manage_channels=True)
    async def deletevoice(self, ctx, channel: discord.VoiceChannel, *, reason=None):
        """Deletes a voice channel."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I have deleted the voice channel **{channel}!**')

    @commands.command(aliases=['dc'])
    @commands.has_permissions(manage_channels=True)
    async def deletecategory(self, ctx, channel: discord.CategoryChannel, *, reason=None):
        """Deletes a category."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I have deleted the category **{channel}!**')

    @commands.command(aliases=['ett'])
    @commands.has_permissions(manage_channels=True)
    async def edittexttopic(self, ctx, channel: discord.TextChannel, *, topic):
        """Edits a text channel's topic."""

        await channel.edit(topic=topic)
        await ctx.send(f"I have edited the text channel {channel.mention}'s topic!")

def setup(bot):
    bot.add_cog(Admin(bot))