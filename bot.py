import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('Donnie is online')


# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


@bot.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in a voice channel")


@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I am not in a voice channel")


bot.run('Token')
