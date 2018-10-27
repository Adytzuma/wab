import discord
import random
from discord.ext import commands
import logging
import traceback
import asyncio
import os
from discord import opus
from asyncio import sleep


class Moderation():
	def __init__(self, bot):
		self.bot = bot
		colors = [discord.Colour.purple(), discord.Colour.blue(), discord.Colour.red(), discord.Colour.green(), discord.Colour.orange()]


	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.group()
	@commands.has_permissions(manage_roles=True)
	async def role(self, ctx):
            """Manage the server roles"""
            if ctx.invoked_subcommand is None:
                return await ctx.send('Hey, please use w!role [add/remove] [role] [member]')




	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member: discord.Member, reason=None):
            """Ban someone"""
            if member == self.bot.user:
                return await ctx.send('I can\'t ban myself.')
            if member == ctx.author:
                return await ctx.send('You can not ban yourself.')
            if member == ctx.guild.owner:
                return await ctx.send('I can\'t ban the server owner')
            if reason is None:
                await member.ban(reason=f'Requested By {ctx.author}')
                return await ctx.send(f'{member} has been succesfully banned!')
            if reason is not None:
                await member.ban(reason=f'{reason} | Requested By {ctx.author}')
                return await ctx.send('{member} was succesfully banned!')


	@commands.cooldown(1, 5, commands.BucketType.user)
	@role.command()
	@commands.has_permissions(manage_roles=True)
	async def remove(self, ctx, role: discord.Role, member: discord.Member):
            """Remove a role from a user"""
            await member.remove_roles(role)
            await ctx.send(f'{member} has lost the " {role} " role')


	@role.command()
	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.has_permissions(manage_roles=True)
	async def add(self, ctx, role: discord.Role, member: discord.Member):
            """Add a role to a user"""
            await member.add_roles(role)
            await ctx.send(f'{member} received the " {role} " role.')





	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, reason=None):
            """Kick someone"""
            if member == self.bot.user:
                return await ctx.send('I can\'t kick myself.')
            if member == ctx.author:
                return await ctx.send('You can not kick yourself.')
            if member == ctx.guild.owner:
                return await ctx.send('I can\'t kick the server owner')
            if reason is None:
                await member.kick(reason=f'Requested By {ctx.author}')
                return await ctx.send(f'{member} has been succesfully kicked!')
            if reason is not None:
                await member.kick(reason=f'{reason} | Requested By {ctx.author}')
                return await ctx.send(f'{member} was kicked succesfully!')


	

        




	

       

        


	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases= ["clear", "prune"])
	@commands.has_permissions(manage_guild=True)
	async def purge(self, ctx, number : int):
		'''Delete a number of messages in a channel'''
		if number>500 or number<0:
			return await ctx.send("Invalid amount, maximum is 500.")
		await ctx.message.delete()
		await ctx.channel.purge(limit=number, bulk=True)
		await ctx.message.channel.send(f'Succesfully deleted {int(number)} messages!', delete_after=5)

	    











def setup(bot):
        bot.add_cog(Moderation(bot))
