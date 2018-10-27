import discord
from discord.ext import commands
import logging
import asyncio
import json
import aiohttp
import random

class Fun():
    def __init__(self, bot):
        self.bot = bot


    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def say(self, ctx, *, message):
        """Make me say something"""
        await ctx.send(message)

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def poll(self, ctx, *, question):
        """Make a poll about something"""
        em = discord.Embed(color=discord.Colour.blurple())
        em.add_field(name='Question:', value=question)
        em.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested By: {ctx.author}')
        a = await ctx.send(embed=em)
        await a.add_reaction('\N{THUMBS UP SIGN}')
        await a.add_reaction('\N{THUMBS DOWN SIGN}')

    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.command()
    async def choose(self, ctx, *options):
        """Make me choose something (If you can't)"""
        if len(options) == 1:
            return await ctx.send('Give me more options dude!')
        a = random.choice(options)
        await ctx.send(f'Hmmm... I\'ll choose " {a} " !')


def setup(bot):
        bot.add_cog(Fun(bot))
