from login import login, comments
from config import configs
from meme import memelist
import re
import time
import discord
import secrets
import time
from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
import random
from config import configs
from discord.ext import commands
from discord.utils import get
import asyncio
from datetime import datetime
import json
from discord.ext.commands import CommandOnCooldown
import urllib.request as req
import bs4
import random
from getpost import post
link = configs['link']
email = configs['email']
password = configs['password']
verifiedrolename = configs['verifiedrolename']
unverifiedrolename = configs['unverifiedrolename']
Invitelink = configs['Invitelink']
prefix = configs['prefix']
verificationchannelname = configs['verificationchannelname']
logchannelname = configs['logchannelname']
client = commands.Bot(command_prefix = prefix)
commenturl = configs['commenturl']
token = configs['token']
verifiedrole = configs['verifiedrolename']
controlchannelname = configs['controlchannelname']
generalchannelname = configs['generalchannelname']
url = configs['url']
memelisthaha = memelist['memelist']




client.remove_command('help')


client.commentToken = {}
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["verifiedusers"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    loggedin = 1
    while (loggedin == 1):
        activity = discord.Game(name=f"{prefix}help | We Are Unity", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Walkers are best friends", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Stop hater Walkers", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Maintain Peace and Unity", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Stop Separatism", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10) #status

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("Insufficient permissions!")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send("Command is on cooldown!")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def verify(ctx):
    WalkerID = {}
    member = ctx.author
    DiscordID = member.id
    WalkerID[DiscordID] = ctx.message.content[4:]
    token = hex(DiscordID)[2:]
    client.commentToken = {}
    client.commentToken[DiscordID] = token[:8] + secrets.token_urlsafe(6) + token[8:]
    stringToken = str(client.commentToken[DiscordID])
    await ctx.channel.send(f"NOTE: This discord bot is **still in development, if you experience errors, please contact Walker #7416.** Please make a comment on the following post exactly as the token below. Then, type `{prefix}go WalkerID(NO #)`, where WalkerID is YOUR OWN WALKER ID. For example if your Walker #7416, you would type `{prefix}go 7416. **IF the bot doesn't respond in 10 seconds to the command `{prefix}go`, there is a problem and you should contact #7416, if it takes a bit longer to respond, then that's completely normal.**"+" <"+str(commenturl) + "> ")
    await ctx.channel.send("copy the token below and paste it in the comments section of the post.")
    await ctx.channel.send(stringToken)
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: verify", color=0x0400ff)
    embed.add_field(name="Action: Generate, store token.", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def hello(ctx):
    member = ctx.author
    await ctx.channel.send('Hello.')
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: hello", color=0x0400ff)
    embed.add_field(name="Action: SayHello", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def invite(ctx):
    await ctx.channel.send("Invite me here! <"+Invitelink+">")
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: invite", color=0x0400ff)
    embed.add_field(name="Action: ShowInviteLink", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def help(ctx):
    member = ctx.author
    embed=discord.Embed(title="Help", color=0x0400ff)
    embed.add_field(name=f"{prefix}help", value="shows this message.", inline=True)
    embed.add_field(name=f"{prefix}invite", value="Invite link for the bot.", inline=True)
    embed.add_field(name=f"{prefix}hello", value="Bot will say Hello.", inline=True)
    embed.add_field(name=f"{prefix}verify", value="Shows instructions for verification, and generates a token to comment on.", inline=True)
    embed.add_field(name=f"{prefix}go", value="The command you type followed by your Walker ID for comment checking purposes. **Does not support DM**", inline=True)
    embed.add_field(name=f"{prefix}unverify", value="The command you type to unverify.", inline=True)
    embed.add_field(name=f"{prefix}say", value="The command you type followed by your desired message to make the bot say that. **Does not support DM**", inline=True)
    embed.add_field(name=f"{prefix}lastverified", value="The command you type to show the last couple users with the user ID and Walker ID, **Admins only**", inline=True)
    embed.add_field(name=f"{prefix}forceverify", value="The command you type to forcefully verify a user followed by a user mention and walker id with space between. **Admins only**")
    embed.add_field(name=f"{prefix}forceunverify", value="The command you type to forcefully unverify a user followed by a user mention. **Admins only**")
    embed.add_field(name=f"{prefix}sourcecode", value="The command you type to make the bot show its source code.")
    embed.add_field(name=f"{prefix}about", value="The command you type to make me say who I am!")
    embed.add_field(name=f"{prefix}servercount", value="The command you type for me to show how many servers I'm in!")
    embed.add_field(name=f"{prefix}serverinvite", value="The command you type for me to invite you to my official server!")
    embed.add_field(name=f"{prefix}donate", value="The command you type to donate for the development of this bot!")
    embed.add_field(name=f"{prefix}website", value="The command you type for the bot to show the link to the website of this bot.")
    embed.add_field(name=f"{prefix}ping", value="The command you type for the bot to show the current ping to the client!")
    embed.add_field(name=f"{prefix}meme", value="The command you type for the bot to show a random meme from the list!")
    embed.set_footer(text="Noice")
    await ctx.channel.send(embed=embed)
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: help", color=0x0400ff)
    embed.add_field(name="Action: Gethelp", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def say (ctx):
    try:
        Content = ctx.message.content[5:]
        await ctx.message.channel.purge(limit = 1)
        await ctx.channel.send(Content)
    except AttributeError:
        await ctx.channel.send("This command does not support DM.")
    except discord.errors.HTTPException:
        await ctx.channel.send(f"What are you making me say? include it after `{prefix}say`!")
    logchannel = discord.utils.get(ctx.author.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: say", color=0x0400ff)
    embed.add_field(name=f"Action: SayCommand({Content})", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        pass

@commands.cooldown(1, 5, commands.BucketType.user)
@client.command()
async def go(ctx): #***ignore this comment*** easypass
    WalkerID = {}
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    DiscordID = member.id
    WalkerID[DiscordID] = ctx.message.content[4:]
    embed=discord.Embed(title="Log: go", color=0x0400ff)
    embed.add_field(name=f"Action: CommentCheck AttemptedID: {WalkerID[DiscordID]}", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")
    await ctx.channel.send("Thanks, I'm checking your comment.")
    #new verify part here
    response = comments([email, password])
    lastComment = response[-1]
    walkerIDFound = lastComment[0]
    tokenFound = lastComment[1]
    print("1)" + tokenFound)
    try:
        print("2)" + client.commentToken[DiscordID])
        if walkerIDFound == WalkerID[DiscordID] and client.commentToken[DiscordID] in tokenFound:
        
            await ctx.channel.send("Verification completed, congrats!")
            role = get(member.guild.roles, name = verifiedrolename)
            unrole = get(member.guild.roles, name = unverifiedrolename)
            WalkerIDnick = "#"+str(WalkerID[DiscordID])
            generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
            mydict = { "WalkerID": int(WalkerID[DiscordID]), "DiscordID": str(DiscordID) }
            x = mycol.insert_one(mydict)
            try:
                await member.add_roles(role)
                await member.remove_roles(unrole)
                await member.edit(nick=WalkerIDnick)
            except discord.errors.Forbidden:
                await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
            try:
                await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
            except AttributeError:
                await ctx.channel.send(f"{ctx.author.guild.owner.mention} I could not find the channel {generalchannelname}, in order for the bot to work properly, please add a channel with that name.")
                await random.choice(ctx.author.guild.text_channels).send(f"Walker {WalkerIDnick} has joined, Welcome!")
            print(DiscordID)  
        else:
            await ctx.channel.send("Could not find your comment, if you did comment, please make sure you commented the token below the link and you entered the correct Walker ID.")

    except:
        await ctx.channel.send(f"You need to do the command {prefix}verify first.")
    print("3)" + walkerIDFound)
    print("4)" + WalkerID[DiscordID])



@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def unverify(ctx):
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    role = get(member.guild.roles, name = verifiedrolename)
    unrole = get(member.guild.roles, name = unverifiedrolename)
    await member.add_roles(unrole)
    await member.remove_roles(role)
    await ctx.channel.send("Unverified.")
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: unverify", color=0x0400ff)
    embed.add_field(name="Action: unverify", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")
    except discord.errors.Forbidden:
        await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
@has_permissions(administrator=True)
async def lastverified(ctx):
        x = mycol.find().sort([('_id', -1)]).limit(6)
        await ctx.channel.send(str(list(x)))
@has_permissions(administrator=True)
@client.command()
async def forceverify(ctx, member: discord.Member):
    current_time = datetime.utcnow()
    WalkerID = {}
    role = get(member.guild.roles, name = verifiedrolename)
    unrole = get(member.guild.roles, name = unverifiedrolename)
    DiscordID = member.id
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    WalkerID[DiscordID] = ctx.message.content[37:]
    generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
    mydict = { "WalkerID": int(WalkerID[DiscordID]), "DiscordID": str(DiscordID) }
    print(WalkerID[DiscordID])
    print(member.guild.name)
    global x
    x = mycol.insert_one(mydict)
    try:
        await ctx.channel.send("Verification completed, congrats!")
        WalkerIDnick = "#"+str(WalkerID[DiscordID])
        await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
        await member.add_roles(role)
        await member.remove_roles(unrole)
        await member.edit(nick=WalkerIDnick)
    except discord.errors.Forbidden:
        await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {member.mention}'s nickname.")
    embed=discord.Embed(title=f"Log: forceverify {WalkerIDnick}", color=0x0400ff)
    embed.add_field(name="Action: forceverify", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")

@has_permissions(administrator=True)
@client.command()
async def forceunverify(ctx, member: discord.Member):
    current_time = datetime.utcnow()
    role = get(member.guild.roles, name = verifiedrolename)
    unrole = get(member.guild.roles, name = unverifiedrolename)
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    try:
        await ctx.channel.send("Unverified.")
        await member.add_roles(unrole)
        await member.remove_roles(role)
    except discord.errors.Forbidden:
        await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
    embed=discord.Embed(title=f"Log: forceunverify", color=0x0400ff)
    embed.add_field(name="Action: forceunverify", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def newposts(ctx):
    embed = discord.Embed(title="Posts List")
    posts = post([email,password])
    for i in posts:
        author = i[0]
        try:
            int(author)
            str(author)
            author = "#" + author
        except:
            pass
        title = i[1]
        link = i[2]
        embed.add_field(name=author, value= f"[{title}]({link})", inline=True)

    await ctx.channel.send(embed=embed)
    
@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def checkpost(ctx, args):
    posts = post([email,password])
    if int(args[0]) < len(posts):
        await ctx.channel.send("Out of range!")
    else:
        await ctx.channel.send("Command is on construction, please try later!") #run...


@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def meme(ctx):
    await ctx.channel.send(random.choice(memelisthaha))


@client.command()
async def sourcecode(ctx):
    await ctx.channel.send("here's the code! https://github.com/junyuxu2006/walkerverificationbot/")

@client.command()
async def about(ctx):
    await ctx.channel.send("This bot is the ONLY Open-source, it has support for ALL Walker IDs, and multi-server compatible. This Walker verification bot is developed by Walker #7416 and it works in Walker Discord servers.")

@client.command()
async def servercount(ctx):
    await ctx.channel.send(f"I'm in {str(len(client.guilds)) } servers!")

@client.command()
async def serverinvite(ctx):
    await ctx.channel.send("Invite for the Green Nexus Walker verification bot official server: https://discord.gg/JhZ6gCw")

@client.command()
async def donate(ctx):
    await ctx.channel.send("https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=SQA2T7K5ACTPJ&item_name=GreenNexusBotSupport&currency_code=USD&source=url")
@client.command()
async def website(ctx):
    await ctx.channel.send("https://greennexus.junyuxu.com/index")

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"ping: {round(client.latency * 1000)} ms")

@client.event
async def on_guild_join(guild):
    await random.choice(guild.text_channels).send(f'{guild.owner.mention} Thanks for adding me. In order for me to properly function, make sure you have a role named "{verifiedrolename}" and "{unverifiedrolename}", and make sure my role is above them. Your server must have a channel  that I can send messages that is named {verificationchannelname}, {logchannelname}, and {generalchannelname}.')

@client.event
async def on_member_join(member):
    unrole = get(member.guild.roles, name = unverifiedrolename)
    channel = discord.utils.get(member.guild.text_channels, name = verificationchannelname)
    await member.add_roles(unrole)
    try:
        await channel.send(f"Welcome{member.mention}. The **{member.guild.name}** server is dedicated to Walkers with an official ID. I'm your friendly verification bot to help you to authorize yourself, getting access to all the Walkers channels on this server in return, please type `{prefix}verify` to get started on your verification process.")
    except AttributeError:
        await random.choice(member.guild.text_channels).send(f"Hey {member.mention}, welcome to **{member.guild.name}**, please type `{prefix}verify` to get started on your verification process.")

client.run(token)
#comments_list = comments(user)
#print(comments_list[-1])
