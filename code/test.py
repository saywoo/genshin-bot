import discord
from discord.ext import commands

# bot token
TOKEN = 'MTA0NjE1OTQ1MDE3NzgwMjMyMQ.GKMKj_._Fa-JxeWDDiRS7yh7pjTvKwGe25IfDYveCEvFo'

intents = discord.Intents.all()

# command_prefix -> %
bot = commands.Bot(command_prefix = "%", intents = intents)

@bot.event
async def on_ready():
    print('[대충 ', bot.user.name, "가 서버에 들어왔다는 말]")

@bot.command()
async def Hello(ctx):
    await ctx.reply("hello world!")

bot.run(TOKEN)
