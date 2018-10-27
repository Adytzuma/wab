import discord
from discord.ext import commands
import logging
import asyncio
import json
import aiohttp
import random
from collections import OrderedDict, deque, Counter
import os, datetime
import asyncio
import copy
import unicodedata
import inspect

class Utility():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def about(self, ctx):
        """Displays info about the bot"""
        async with aiohttp.ClientSession() as cs:      
            async with cs.get('https://raw.githubusercontent.com/Adytzuma/no-dont-look/master/info.json') as r:
                load = await r.json(content_type=None)
                owner = load['data']['owner']
                version = load['data']['version']
                pythonVersion = load['data']['pythonVersion']
                discordVersion = load['data']['discord.py']
                language = load['data']['language']
                
                a = discord.Embed(color=discord.Colour.blurple())
                a.add_field(name='Owner', value=owner)
                a.add_field(name='Bot Version', value=version)
                a.add_field(name='Language', value=language)
                a.add_field(name='Python Version', value=pythonVersion + '(discord.py)')
                a.add_field(name='Discord.py Version', value=discordVersion)
                a.add_field(name='Users', value=f'{len(self.bot.users)}')
                a.set_thumbnail(url=ctx.me.avatar_url)
                return await ctx.send(embed=a)


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def serverinfo(self, ctx):
        """Show info about the current server"""
        total = ctx.guild.member_count
        bot = 0
        members = 0
        for i in ctx.guild.members:
            if i.bot is True:
                bot+=1
            if i.bot is False:
                members+=1

       
        a = discord.Embed(color=discord.Colour.blurple())
        a.add_field(name='Owner:', value=ctx.guild.owner)
        a.add_field(name='ID:', value=f'{ctx.guild.id}')
        a.add_field(name=f'Members [{total}]:', value=f'{members} humans\n{bot} bots')
        a.add_field(name='Channels:', value=f'{len(ctx.guild.channels)}')
        a.add_field(name='Icon:', value=f'[Here]({ctx.guild.icon_url})')
        a.add_field(name='Roles:', value=f'{len(ctx.guild.roles)}')
        a.add_field(name='Region:', value=f'{ctx.guild.region}')
        a.set_footer(text=f'Created At: {ctx.guild.created_at.strftime("%d/%m/%Y")}')
 
        a.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=a)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['char'])
    async def charinfo(self, ctx, *, characters: str):
        """Shows information about a caracter"""
        def to_string(c):
            digit = f'{ord(c):x}'
            name = unicodedata.name(c, 'Name could not be found.')
            return f'**{c}** | ``\\U{digit:>08}`` | {name}'
        msg = '\n'.join(map(to_string, characters))
        if len(msg) > 750:
            return await ctx.send('Output too long to display')
        await ctx.send(msg)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def userinfo(self, ctx, user: discord.Member=None):
        """Show info about a user"""
        if user is None:
            user = ctx.author
        a = discord.Embed(color=discord.Colour.blurple())
        a.add_field(name='Name:', value=user.name)
        a.add_field(name='ID:', value=f'{user.id}')
        a.add_field(name='Bot:', value=user.bot)
        a.add_field(name='Nick:', value=user.nick)
        a.add_field(name='Top Role:', value=user.top_role)
        a.add_field(name='Avatar:', value=f'[Here]({user.avatar_url})')
        a.set_thumbnail(url=user.avatar_url)
        a.add_field(name='Account Created At:', value=f'{user.created_at.strftime("%A, %B  %Y (%d/%m/%Y)")}')
        await ctx.send(embed=a)


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def emoji(self, ctx, emoji: discord.Emoji):
        """Show information about an emoji"""
        await ctx.send(f'`Name:` {emoji.name}\n`ID:` {emoji.id}\n`Preview:` {emoji} (`{emoji}`)\n`URL:` {emoji.url}\n`Added at:` {emoji.created_at.strftime("%A, %B %Y")}')





def setup(bot):
        bot.add_cog(Utility(bot))
       
