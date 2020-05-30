import discord
from discord.ext import commands

class Admin(commands.Cog, name='Administration Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['er'])
    @commands.has_permissions(manage_roles=True)
    async def editrole(self, ctx, role, args, *, args2):
        """Edits a role."""

        role=discord.utils.get(ctx.guild.roles, name=f'{role}')
        
        if args == 'name':

            name = args2

        if args != 'name':

            name = f'{role.name}'

        if args == 'color':

            color = args2

            if "#" in color:
                color = color.replace("#", "")

            col = discord.Color(value=int(color, 16))

        if args != 'color':
                
            col = role.color

        if args == 'position':

            position = int(args2)

        if args != 'position':

            position = role.position

        await role.edit(name=name, color=col, position=position)
        await ctx.send(f'I edited the role **{role.name}**!')

    @commands.command(aliases=['cr'])
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, *, name):
        """Creates a role."""

        await ctx.guild.create_role(name=name)
        await ctx.send(f'I created the role **{name}**!')

    @commands.command(aliases=['dr'])
    @commands.has_permissions(manage_roles=True)
    async def deleterole(self, ctx, role: discord.Role):
        """Deletes a role."""

        await role.delete()
        await ctx.send(f'I deleted the role **{role}**!')

    @commands.command(aliases=['ct'])
    @commands.has_permissions(manage_channels=True)
    async def createtext(self, ctx, *, channel):
        """Creates a text channel."""

        await ctx.guild.create_text_channel(name=channel)
        await ctx.send(f'I created the text channel **{channel}**!')

    @commands.command(aliases=['cv'])
    @commands.has_permissions(manage_channels=True)
    async def createvoice(self, ctx, *, channel):
        """Creates a voice channel."""

        await ctx.guild.create_voice_channel(name=channel)
        await ctx.send(f'I created the voice channel **{channel}**!')

    @commands.command(aliases=['cc'])
    @commands.has_permissions(manage_channels=True)
    async def createcategory(self, ctx, *, channel):
        """Creates a category."""

        await ctx.guild.create_category_channel(name=channel)
        await ctx.send(f'I created the category **{channel}**!')

    @commands.command(aliases=['et'])
    @commands.has_permissions(manage_channels=True)
    async def edittextname(self, ctx, channel: discord.TextChannel, *, name):
        """Edits a text channel name."""

        await channel.edit(name=name)
        await ctx.send(f"I edited the text channel **{channel}**!")

    @commands.command(aliases=['ev'])
    @commands.has_permissions(manage_channels=True)
    async def editvoicename(self, ctx, channel: discord.VoiceChannel, *, name):
        """Edits a voice channel name."""

        await channel.edit(name=name)
        await ctx.send(f"I edited the voice channel **{channel}**!")

    @commands.command(aliases=['ec'])
    @commands.has_permissions(manage_channels=True)
    async def editcategoryname(self, ctx, channel: discord.CategoryChannel, *, name):
        """Edits a category name."""

        await channel.edit(name=name)
        await ctx.send(f"I edited the category **{channel}**!")

    @commands.command(aliases=['mt'])
    @commands.has_permissions(manage_channels=True)
    async def movetext(self, ctx, channel: discord.TextChannel, *, category: discord.CategoryChannel):
        """Moves a text channel."""

        await channel.edit(category=category)
        await ctx.send(f'I moved the text channel **{channel}**!')

    @commands.command(aliases=['mv'])
    @commands.has_permissions(manage_channels=True)
    async def movevoice(self, ctx, channel: discord.VoiceChannel, *, category: discord.CategoryChannel):
        """Moves a voice channel."""

        await channel.edit(category=category)
        await ctx.send(f'I moved the voice channel **{channel}**!')

    @commands.command(aliases=['dt'])
    @commands.has_permissions(manage_channels=True)
    async def deletetext(self, ctx, channel: discord.TextChannel, *, reason=None):
        """Deletes a text channel."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I deleted the text channel **{channel}**!')

    @commands.command(aliases=['dv'])
    @commands.has_permissions(manage_channels=True)
    async def deletevoice(self, ctx, channel: discord.VoiceChannel, *, reason=None):
        """Deletes a voice channel."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I deleted the voice channel **{channel}**!')

    @commands.command(aliases=['dc'])
    @commands.has_permissions(manage_channels=True)
    async def deletecategory(self, ctx, channel: discord.CategoryChannel, *, reason=None):
        """Deletes a category."""
        
        ctx.guild.get_channel(channel)
        
        await channel.delete(reason=reason)
        await ctx.send(f'I deleted the category **{channel}**!')

    @commands.command(aliases=['ett'])
    @commands.has_permissions(manage_channels=True)
    async def edittexttopic(self, ctx, channel: discord.TextChannel, *, topic):
        """Edits a text channel topic."""

        await channel.edit(topic=topic)
        await ctx.send(f"I edited the text channel **{channel.mention}**!")

def setup(bot):
    bot.add_cog(Admin(bot))