import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(level='INFO')
prefix = ['w!', 'W!']
bot = commands.Bot(case_insensitive=True, command_prefix=prefix)
bot.load_extension('cogs.gen')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.admin')
bot.load_extension('cogs.meta')
bot.load_extension('cogs.utility')
bot.load_extension('cogs.mod')



@bot.event
async def on_ready():
    print(f'Logging in as {bot.user.name}.')
    await bot.change_presence(activity=discord.Game(name="with the WaB members | w!help"))


@bot.check
async def nobotspls(ctx):
    return not ctx.author.bot






@bot.event
async def on_command_error(ctx, error):
    if ctx.author.bot is True:
        return
    return await ctx.send(f':x: | {error}')

#===============================
"""
@bot.event
async def on_member_join(member):
    if member.guild.id != 503156610248605698:
        return
    em = discord.Embed(color=discord.COlour.green())
    em.add_field(name=':tada: | Welcome!', value=member.mention)
    em.add_field(name=':tools: | Info:', value='Hello, welcome into the server! Ping <@&503159799123279894> for help. If you want to join our clan check out <#503157422957789205> ! Enjoy!')
    em.set_thumbnail(url=member.avatar_url)
    await bot.get_guild(503156610248605698).get_channel(391896622625456159).send(embed=em)
    
    

@bot.event
async def on_member_join(member):
    if member.guild.id != 503156610248605698:
        return
    em = discord.Embed(color=discord.COlour.green())
    em.add_field(name=':cry: | Goodbye!', value=member)
    em.add_field(name=':tools: | Info:', value='He left us, I hope he joins back.')
    em.set_thumbnail(url=member.avatar_url)
    await bot.get_guild(503156610248605698).get_channel(391896622625456159).send(embed=em)
"""
#===============================

bot.run(os.getenv("TOKEN"))


