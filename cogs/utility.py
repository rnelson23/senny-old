import discord
import asyncio
from discord.ext import commands
from datetime import datetime as d

class utility(commands.Cog, name='Utillity Commands'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Checks pingtime"""

        start = d.timestamp(d.now())
        msg = await ctx.send(content='Pinging')

        await msg.edit(content=f'Pong! **{round((d.timestamp(d.now()) - start) * 1000)}ms**')

    @commands.command()
    async def temp(self, ctx, num: int, unit: str):
        """Converts temp units"""

        if unit == 'F':
            resultc = round((num - 32) * (5/9))
            await ctx.send(f'**{num}°F** is **{resultc}°C**')

        if unit == 'C':
            resultf = round((num * (9/5)) + 32)
            await ctx.send(f'**{num}°C** is **{resultf}°F**')

    @commands.command(aliases=['dis', 'd'])
    async def disboard(self, ctx):
        """Reminds to bump"""

        await ctx.send(f"Alright, {ctx.author.mention}, I'll remind {ctx.channel.mention} about **!d bump** in 2 hours!")
        await asyncio.sleep(7200)
        await ctx.send(f'Hey, 2 hours ago, you asked me to remind {ctx.channel.mention} about **!d bump**!')

    @commands.command(aliases= ['rmd', 'r'])
    async def remind(self, ctx, place, time=None, *, reason=None):
        """Reminds a user/channel"""

        converter = (time[-1])
        amount2 = (time[:-1])

        def amount(self, time):
            try:
                return int(time[:-1])
            except:
                return time

        if converter == "s":
            duration = (amount(self, time) * 1)
            if amount2 == '1':
                duration2 = f'{amount2} second'
            elif amount2 != '1':
                duration2 = f'{amount2} seconds'


        if converter == 'm':
            duration = (amount(self, time) * 60)
            if amount2 == '1':
                duration2 = f'{amount2} minute'
            elif amount2 != '1':
                duration2 = f'{amount2} minutes'

        if converter == 'h':
            duration = (amount(self, time) * 3600)
            if amount2 == '1':
                duration2 = f'{amount2} hour'
            elif amount2 != '1':
                duration2 = f'{amount2} hours'

        if converter == 'd':
            duration = (amount(self, time) * 86400)
            if amount2 == '1':
                duration2 = f'{amount2} day'
            elif amount2 != '1':
                duration2 = f'{amount2} days'

        if place == 'me':
            
            user = ctx.author
            channel2 = await user.create_dm()

            await ctx.send(f"Alright, {user.mention}, I'll remind you about **{reason}** in {duration2}!")
            await asyncio.sleep(duration)
            await channel2.send(f"Hey, {duration2} ago, you asked me to remind you about **{reason}**!")

        elif place == 'here':

            user = ctx.author
            channel = ctx.channel

            await ctx.send(f"Alright, {user.mention}, I'll remind {channel.mention} about **{reason}** in {duration2}!")
            await asyncio.sleep(duration)
            await channel.send(f"Hey, {duration2} ago, you asked me to remind {channel.mention} about **{reason}**!")
            
            return

    @commands.command()
    async def jumbo(self, ctx, emoji: discord.PartialEmoji):
        """Gets an emote"""

        embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

        embed.set_author(name=f'Emoji - {emoji.name}', url=emoji.url)
        embed.set_image(url=emoji.url)
        embed.set_footer(text=f'Requested by {ctx.author}')

        await ctx.send(embed=embed)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, user: discord.User=None):
        """Gets an avatar"""

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

    @commands.command(aliases=['info'])
    async def userinfo(self, ctx, user: discord.Member=None):
        """Shows user info"""

        if user is None:
            user = ctx.author

            roles = user.roles
            roles = [role.mention for role in roles if role.name != '@everyone']
            roles.reverse()

            join_position = sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1

            status = "Web: " + str(user.web_status) + "\nDesktop: " + str(user.desktop_status) + "\nMobile: " + str(user.mobile_status)

            perms = iter(ctx.channel.permissions_for(user))
            perms_we_have = ""
            for x in perms:
               if "True" in str(x):
                   perms_we_have += "{0}\n".format(str(x).split("'")[1])

            message = "\n"

            if not user.activity or not user.activities:
                message = "N/A"

            for activity in user.activities:

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
                        message += f"Listening to **{activity.name}**\n"

            if user.premium_since is None:
                booster = 'No'
            else:
                time = user.premium_since.__format__('%B %d, %Y @ %H:%M')
                booster = f'Since {time}'

            embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=f'{user} ~ {user.display_name}', url=user.avatar_url)
            embed.add_field(name='Joined Discord on', value=user.created_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Joined server on', value=user.joined_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
            embed.add_field(name='Join Position', value=join_position, inline=False)
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

            join_position = sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1

            status = "Web: " + str(user.web_status) + "\nDesktop: " + str(user.desktop_status) + "\nMobile: " + str(user.mobile_status)

            perms = iter(ctx.channel.permissions_for(user))
            perms_we_have = ""
            for x in perms:
               if "True" in str(x):
                   perms_we_have += "{0}\n".format(str(x).split("'")[1])

            message = "\n"

            if not user.activity or not user.activities:
                message = "N/A"

            for activity in user.activities:

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
            embed.add_field(name='Join Position', value=join_position, inline=False)
            embed.add_field(name='Status', value=status, inline=False)
            embed.add_field(name='Activity', value=message, inline=False)
            embed.add_field(name='Is Bot?', value=user.bot, inline=False)
            embed.add_field(name='Color', value=user.color, inline=False)
            embed.add_field(name='Booster?', value=booster, inline=False)
            embed.add_field(name='Guild Permissions', value=perms_we_have, inline=False)
            embed.add_field(name='Roles', value=' '.join(roles), inline=False)
            embed.set_footer(text=f'User ID: {user.id}')
            
            await ctx.send(embed=embed)

    @commands.command(aliases=['server'])
    async def serverinfo(self, ctx):
        """Shows server info"""

        embed = discord.Embed(color = 0x3a86ff, timestamp=ctx.message.created_at)

        embed.set_author(name=f'Server Info - {ctx.author.guild.name}', url=f'{ctx.author.guild.icon_url}')
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_image(url=ctx.author.guild.splash_url)
        embed.add_field(name='Owner', value=f'{ctx.author.guild.owner}', inline=False)
        embed.add_field(name='Created on', value=ctx.author.guild.created_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
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

    @commands.command(aliases=['role'])
    async def roleinfo(self, ctx, *, role: discord.Role):
        """Shows role info"""
        
        embed = discord.Embed(color=0x3a86ff, timestamp=ctx.message.created_at)

        perms = iter(role.permissions)
        message = "none\n"
        for x in perms:
            if "True" in str(x):
                message += "{0}\n".format(str(x).split("'")[1])

        embed.set_author(name=f'Role Info - {role.name}')
        embed.add_field(name='Created on', value=role.created_at.__format__('%B %d, %Y @ %H:%M'), inline=False)
        embed.add_field(name='Mentionable?:', value=role.mentionable, inline=False)
        embed.add_field(name='Hoisted?', value=role.hoist, inline=False)
        embed.add_field(name='Color', value=role.color, inline=False)
        embed.add_field(name='In role', value=f'{len(list(role.members))} members', inline=False)
        embed.add_field(name='Permissions', value=f'{message}', inline=False)
        embed.set_footer(text=f'Role ID: {role.id}')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(utility(bot))