import discord
from discord.ext import commands
import logging
import asyncio
import json
import aiohttp
import random

class NameGenerators():
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['fortnite'])
    async def fortnitename(self, ctx):
        """Generates a random Fortnite name (genr8rs.com's API)"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.genr8rs.com/Generator/Gaming/Fortnite/NameGenerator?genr8rsUserId=1536674547.43325b97caf369c4b&_sNameLength=medium') as r:
                load = await r.json(content_type=None)
                name = load['_sResult']
                await ctx.send(f'Your random Fortnite name is:\n{name}')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['fwd', 'forwardassault', 'forwardassaultname'])
    async def fwdname(self, ctx):
        """Generates a random Forward Assault name (genr8rs.com's API)"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.genr8rs.com/Generator/Gaming/Csgo/NameGenerator?genr8rsUserId=1536674547.43325b97caf369c4b&_sNameLength=medium') as r:
                load = await r.json(content_type=None)
                name = load['_sResult']
                await ctx.send(f'Your random Forward Assault name is:\n{name}')
    

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['pubg'])
    async def pubgname(self, ctx):
        """Generates a random PUBG name (genr8rs.com's API)"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.genr8rs.com/Generator/Gaming/PUBG/NameGenerator?genr8rsUserId=1536674547.43325b97caf369c4b&_sNameLength=short') as r:
                load = await r.json(content_type=None)
                name = load['_sResult']
                await ctx.send(f'Your random PUBG name is:\n{name}')


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command(aliases=['clan'])
    async def clanname(self, ctx, leaderName=None):
        """Generates a random clan name (genr8rs.com's API)"""
        if leaderName is None:
            leaderName = ctx.author.name
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.genr8rs.com/Generator/Gaming/Fun/ClanNameGenerator?genr8rsUserId=1536674547.43325b97caf369c4b&_sLeaderName={leaderName}&_sCountryCode=US&_sNameLength=long') as r:
                load = await r.json(content_type=None)
                name = load['_sName']
                tag = load['_sTag']
                await ctx.send(f'{leaderName}\'s clan name is:\n{tag} {name}')




def setup(bot):
        bot.add_cog(NameGenerators(bot))
 
