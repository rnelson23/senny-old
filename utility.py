import discord
import asyncio
import datetime
import math
from discord.ext import commands
from datetime import datetime as d

class UtiCog(commands.Cog, name='Utillity Commands'):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ping(self, ctx):
        """Gives the bot's ping"""

        start = d.timestamp(d.now())
        msg = await ctx.send(content='Pinging')

        await msg.edit(content=f'Pong! **{round((d.timestamp(d.now()) - start) * 1000)}ms**')

    @commands.command()
    async def temp(self, ctx, num: int, unit: str):
        """Converts between F and C"""

        if unit == 'F':
            resultc = round((num - 32) * (5/9))
            await ctx.send(f'**{num}°F** is **{resultc}°C**')

        if unit == 'C':
            resultf = round((num * (9/5)) + 32)
            await ctx.send(f'**{num}°C** is **{resultf}°F**')

    @commands.command()
    async def jumbo(self, ctx, emoji: discord.PartialEmoji):
        """Gives an emote's image"""

        embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

        embed.set_author(name=f'Emoji - {emoji.name}', url=emoji.url)
        embed.set_image(url=emoji.url)
        embed.set_footer(text=f'Requested by {ctx.author}')

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, user: discord.User=None):
        """Displays a user's avatar"""

        if user is None:
            user = ctx.author
 
            embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)
            
            embed.set_author(name=f'User Avatar - {user}', url=user.avatar_url)            
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=f'Requested by {ctx.author}')
           
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)        
            
            embed.set_author(name=f'User Avatar - {user}', url=user.avatar_url)
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=f'Requested by {ctx.author}')

            await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, user: discord.Member=None):
        """Displays a user's information."""

        if user is None:
            user = ctx.author

            roles = user.roles
            roles = [role.mention for role in roles if role.name != '@everyone']
            roles.reverse()

            perms = iter(ctx.channel.permissions_for(user))
            perms_we_have = ""
            for x in perms:
               if "True" in str(x):
                   perms_we_have += "{0}\n".format(str(x).split("'")[1])

            message = "\n"

            if not user.activity or not user.activities:
                message = "N/A"

            for activity in user.activities:

                # Type 4 is custom status, ignore
                if activity.type == discord.ActivityType.custom:
                    if activity.emoji is None:
                        emoji = ''
                    else:
                        emoji = activity.emoji
                    
                    message += f'\n**Custom Status**\n{emoji} {activity.name}\n'

                elif activity.type == discord.ActivityType.playing:

                    message += f"\n**Playing a Game**\n{activity.name}"
                    if not isinstance(activity, discord.Game):
                        if activity.details:
                            message += f"\n{activity.details}"
                        if activity.state:
                            message += f"\n{activity.state}"

                        message += "\n"

                elif activity.type == discord.ActivityType.streaming:
                    message += f"\n**Live on {activity.platform}**\nStreaming [{activity.name}]({activity.url})\n"

                elif activity.type == discord.ActivityType.watching:
                    message += f"\n**Watching {activity.name}**\n"

                elif activity.type == discord.ActivityType.listening:

                    if isinstance(activity, discord.Spotify):
                        url = f"https://open.spotify.com/track/{activity.track_id}"
                        message += f"\n**Listening to Spotify**\n[{activity.title}]({url})\nby {', '.join(activity.artists)}"
                        if activity.album and not activity.album == activity.title:
                            message += f"\non {activity.album}"
                        message += "\n"
                    else:
                        message += f"• Listening to **{activity.name}**\n"

            if user.is_on_mobile() == True:
                status = f'{user.status} on mobile'
            else:
                status = f'{user.status} on desktop'

            if user.premium_since is None:
                booster = 'No'
            else:
                time = user.premium_since.__format__('%B %d, %Y @ %H:%M')
                booster = f'Since {time}'

            embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=f'{user} ~ {user.display_name}', url=user.avatar_url)
            embed.add_field(name='Joined Discord on', value=user.created_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Joined this server on', value=user.joined_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Status', value=status, inline=False)
            embed.add_field(name='Activity', value=message, inline=False)
            embed.add_field(name='Is Bot?', value=user.bot, inline=False)
            embed.add_field(name='Color', value=user.color, inline=False)
            embed.add_field(name='Booster?', value=booster, inline=False)
            embed.add_field(name='Guild Permissions', value=perms_we_have, inline=False)
            embed.add_field(name='Roles', value=' '.join(roles), inline=False)
            embed.set_footer(text=f'User ID: {user.id}')
            
            await ctx.send(embed=embed)

        else:
            roles = user.roles
            roles = [role.mention for role in roles if role.name != '@everyone']
            roles.reverse()

            perms = iter(ctx.channel.permissions_for(user))
            perms_we_have = ""
            for x in perms:
               if "True" in str(x):
                   perms_we_have += "{0}\n".format(str(x).split("'")[1])

            message = "\n"

            if not user.activity or not user.activities:
                message = "N/A"

            for activity in user.activities:

                # Type 4 is custom status, ignore
                if activity.type == discord.ActivityType.custom:
                    if activity.emoji is None:
                        emoji = ''
                    else:
                        emoji = activity.emoji
                    
                    message += f'\n**Custom Status**\n{emoji} {activity.name}\n'

                elif activity.type == discord.ActivityType.playing:

                    message += f"\n**Playing a Game**\n{activity.name}"
                    if not isinstance(activity, discord.Game):
                        if activity.details:
                            message += f"\n{activity.details}"
                        if activity.state:
                            message += f"\n{activity.state}"

                        message += "\n"

                elif activity.type == discord.ActivityType.streaming:
                    message += f"\n**Live on {activity.platform}**\nStreaming [{activity.name}]({activity.url})\n"

                elif activity.type == discord.ActivityType.watching:
                    message += f"\n**Watching {activity.name}**\n"

                elif activity.type == discord.ActivityType.listening:

                    if isinstance(activity, discord.Spotify):
                        url = f"https://open.spotify.com/track/{activity.track_id}"
                        message += f"\n**Listening to Spotify**\n[{activity.title}]({url})\nby {', '.join(activity.artists)}"
                        if activity.album and not activity.album == activity.title:
                            message += f"\non {activity.album}"
                        message += "\n"
                    else:
                        message += f"• Listening to **{activity.name}**\n"

            if user.is_on_mobile() == True:
                status = f'{user.status} on mobile'
            else:
                status = f'{user.status} on desktop'

            if user.premium_since is None:
                booster = 'No'
            else:
                time = user.premium_since.__format__('%B %d, %Y @ %H:%M')
                booster = f'Since {time}'

            embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=f'{user} ~ {user.display_name}', url=user.avatar_url)
            embed.add_field(name='Joined Discord on', value=user.created_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Joined this server on', value=user.joined_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Status', value=status, inline=False)
            embed.add_field(name='Activity', value=message, inline=False)
            embed.add_field(name='Is Bot?', value=user.bot, inline=False)
            embed.add_field(name='Color', value=user.color, inline=False)
            embed.add_field(name='Booster?', value=booster, inline=False)
            embed.add_field(name='Guild Permissions', value=perms_we_have, inline=False)
            embed.add_field(name='Roles', value=' '.join(roles), inline=False)
            embed.set_footer(text=f'User ID: {user.id}')
            
            await ctx.send(embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        """Displays server information."""

        embed = discord.Embed(color = 0x3a86ff, timestamp=ctx.message.created_at)

        embed.set_author(name=f'Server Info - {ctx.author.guild.name}', url=f'{ctx.author.guild.icon_url}')
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_image(url=ctx.author.guild.splash_url)
        embed.add_field(name='Owner', value=f'{ctx.author.guild.owner}', inline=False)
        embed.add_field(name='Created on', value=ctx.author.guild.created_at.__format__('%B %d, %Y at %H:%M'), inline=False)
        embed.add_field(name='Total Member Count', value=f'{len(list(ctx.author.guild.members))} Members', inline=False)
        embed.add_field(name='Total Nitro Boosters', value=f'{ctx.author.guild.premium_subscription_count} Boosters', inline=False)
        embed.add_field(name='Channels', value=f'{len(list(ctx.author.guild.text_channels))} Text Channels')
        embed.add_field(name='Region', value=ctx.author.guild.region, inline=False )
        embed.add_field(name='2FA Level', value=ctx.author.guild.mfa_level, inline=False)
        embed.add_field(name='Explicit Content Level', value=ctx.author.guild.explicit_content_filter, inline=False)
        embed.add_field(name='Default Notifications Level', value=ctx.author.guild.default_notifications, inline=False)
        embed.add_field(name='System Channel', value=ctx.author.guild.system_channel, inline=False)
        embed.set_footer(text=f'Server ID: {ctx.author.guild.id}')
        
        await ctx.send(embed=embed)

    @commands.command()
    async def roleinfo(self, ctx, *, role: discord.Role):
        """Displays role information."""
        
        embed = discord.Embed(timestamp=ctx.message.created_at, color = role.color)

        embed.set_author(name=f'Role Info - {role.name}', url=ctx.author.avatar_url)
        embed.add_field(name='Role ID:', value=role.id, inline=False)
        embed.add_field(name='Role Creation Date:', value=role.created_at.__format__('%b %d %Y %H:%M'), inline=False)
        embed.add_field(name='Role Position Integer:', value=role.position, inline=False)
        embed.add_field(name='Mentionable?:', value=role.mentionable, inline=False)
        embed.add_field(name='Role Hoist:', value=role.hoist, inline=False)
        embed.add_field(name='Role Color:', value=role.color, inline=False)
        embed.add_field(name='Role Members:', value=f'{len(list(role.members))}', inline=False)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.guild_only()
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def perms(self, ctx, user: discord.Member = None):
        """Fetch a specific user's permissions."""

        if user is None:
            user = ctx.author

        perms = iter(ctx.channel.permissions_for(user))
        perms_we_have = ""
        perms_we_dont = ""
        for x in perms:
            if "True" in str(x):
                perms_we_have += "+\t{0}\n".format(str(x).split("'")[1])
            else:
                perms_we_dont += "-\t{0}\n".format(str(x).split("'")[1])
        await ctx.send(f'```diff\n{perms_we_have}{perms_we_dont}```')

def setup(bot):
    bot.add_cog(UtiCog(bot))