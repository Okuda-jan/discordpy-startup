from discord.ext import commands
import os
import traceback
#import discord #discord.pyの読み込み

bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@client.command()
async def ping(ctx):
    await ctx.send('pong')

client.run(token)
