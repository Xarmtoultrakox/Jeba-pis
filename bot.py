import discord
from discord.ext import commands
import random
from random import randint
import datetime



client = commands.Bot(command_prefix = '!', help_command=None)


@client.event
async def on_ready():
    time = datetime.datetime.now()
    print("Online at {}".format(time))

    acts = client.guilds
    mem = 0

    print("\nServers:")
    for s in acts:
        print(str(s.name))
        
    if str(s.name) == "Discord Bot List":
        return

    for a in acts:
        mem += len(a.members)

    print("\nMembers:", mem)
    
    await client.change_presence(activity=discord.Game(name='!meme'.format(mem)))

@client.command()
async def help(ctx):
    embed=discord.Embed(title="komendy")
    embed.add_field(name="undefined", value="undefined", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def meme(ctx):
    num = randint(1, 12)
    try:
        await ctx.send(file = discord.File("MEMES/{}.jpg".format(num))) 
    except:
        await ctx.send(file = discord.File("MEMES/{}.png".format(num)))

client.run('twuj token')