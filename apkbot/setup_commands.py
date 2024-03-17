# commands.py
from discord.ext import commands

def setup_commands(bot):
    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')
