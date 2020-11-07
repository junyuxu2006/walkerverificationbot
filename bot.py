from login import login, comments, post, post_contents, searchPost
from config import configs
from meme import memelist
import re
import time
import discord
import secrets
import time
from discord.ext.commands import Bot, Cog, command, has_permissions, MissingPermissions, CommandOnCooldown
from discord.ext import commands
import random
from config import configs
from discord.ext import commands, tasks
from discord.utils import get
import asyncio
from datetime import datetime
import urllib.request as req
import json
import googletrans
from googletrans import Translator
import traceback
import threading
import requests
from bs4 import BeautifulSoup
import logging
import dbl
link = configs['link']
email = configs['email']
password = configs['password']
verifiedrolename = configs['verifiedrolename']
unverifiedrolename = configs['unverifiedrolename']
Invitelink = configs['Invitelink']
prefix = configs['devprefix']
verificationchannelname = configs['verificationchannelname']
logchannelname = configs['logchannelname'] 
commenturl = configs['commenturl']
allposts= configs['allposts']
token = configs['devtoken']
verifiedrole = configs['verifiedrolename']
controlchannelname = configs['controlchannelname']
generalchannelname = configs['generalchannelname']
url = configs['url']
memelisthaha = memelist['memelist']
devids = configs['devids']
topggtoken = configs['topggtoken']
intents = discord.Intents.default()
intents.members = False
Bot = commands.Bot(command_prefix=prefix, intents=intents)

Bot.remove_command('help')


Bot.commentToken = {}
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["verifiedusers"]
myservers = mydb["servers"]
#moving to test.py
@Bot.event
async def on_ready():
    print(f'We have logged in as {Bot.user}')
    loggedin = 1
    while (loggedin == 1):
        activity = discord.Game(name=f"{prefix}help | We Are Unity", type=3)
        await Bot.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Walkers are best friends", type=3)
        await Bot.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Stop hater Walkers", type=3)
        await Bot.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Maintain Peace and Unity", type=3)
        await Bot.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f"{prefix}help | Stop Separatism", type=3)
        await Bot.change_presence(activity=activity)
        await asyncio.sleep(10)

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.channel.send("Insufficient permissions!")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send("Command is on cooldown!")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def verify(ctx):
    member = ctx.author
    DiscordID = member.id
    token = hex(DiscordID)[2:] #stop scrolling for a sec LMFAO
    Bot.commentToken = {}
    Bot.commentToken[DiscordID] = token[:8] + secrets.token_urlsafe(6) + token[8:]
    stringToken = str(Bot.commentToken[DiscordID])
    async with ctx.channel.typing():
        await asyncio.sleep(5)
        await ctx.channel.send(f"NOTE: This discord bot is **still in development, if you experience errors, please contact Walker #7416.** Please make a comment on the following post exactly as the token below. Then, type `{prefix}go WalkerID(NO #)`, where WalkerID is YOUR OWN WALKER ID. For example if your Walker #7416, you would type `{prefix}go 7416`. **IF the bot doesn't respond in 10 seconds to the command `{prefix}go`, there is a problem and you should contact #7416, if it takes a bit longer to respond, then that's completely normal.**"+" <"+str(commenturl) + "> ")
        await ctx.channel.send("copy the token below and paste it in the comments section of the post.")
        await ctx.channel.send(stringToken)
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: verify", color=0x0400ff)
    embed.add_field(name="Action: Generate, store token.", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")


@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def hello(ctx):
    member = ctx.author
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send('Hello.')
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: hello", color=0x0400ff)
    embed.add_field(name="Action: SayHello", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def invite(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("Invite me here! <"+Invitelink+">")
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: invite", color=0x0400ff)
    embed.add_field(name="Action: ShowInviteLink", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def help(ctx, args=None):
    passed = 0
    try:
        embed=discord.Embed(title=f"help ({args})", color=0x0400ff)
        if args == None:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send(f"Your options are: `verfication`, `info`, `mod`, `platform`, `translate`, `fun`, `dev` or `misc`. Please put one of these options after {prefix}help.")
        if args == 'verification':
            embed.add_field(name=f"{prefix}verify", value="Shows instructions for verification, and generates a token to comment on.", inline=True)
            embed.add_field(name=f"{prefix}go", value="The command you type followed by your Walker ID for comment checking purposes. **Does not support DM**", inline=True)
            embed.add_field(name=f"{prefix}unverify", value="The command you type to unverify.", inline=True)
            embed.add_field(name=f"{prefix}lastverified", value="The command you type to show the last couple users with the user ID and Walker ID, **Admins only**", inline=True)
            embed.add_field(name=f"{prefix}forceverify", value="The command you type to forcefully verify a user followed by a user mention and walker id with space between. **Admins only**")
            embed.add_field(name=f"{prefix}forceunverify", value="The command you type to forcefully unverify a user followed by a user mention. **Admins only**")
            passed = 1
        if args == 'info':
            embed.add_field(name=f"{prefix}invite", value="Invite link for the bot.", inline=True)
            embed.add_field(name=f"{prefix}sourcecode", value="The command you type to make the bot show its source code.")
            embed.add_field(name=f"{prefix}about", value="The command you type to make me say who I am!")
            embed.add_field(name=f"{prefix}servercount", value="The command you type for me to show how many servers I'm in!")
            embed.add_field(name=f"{prefix}serverinvite", value="The command you type for me to invite you to my official server!")
            embed.add_field(name=f"{prefix}donate", value="The command you type to donate for the development of this bot!")
            embed.add_field(name=f"{prefix}vote", value="The command you type to vote to show your support of me!")
            embed.add_field(name=f"{prefix}website", value="The command you type for the bot to show the link to the website of this bot.")
            embed.add_field(name=f"{prefix}ping", value="The command you type for the bot to show the current ping to the Bot!")
            embed.add_field(name=f"{prefix}usercount", value="The command you type for the bot to show the current number of Walker Discord accounts verified with this bot!")
            embed.add_field(name=f"{prefix}contact", value="The command you type for the bot to show you the contact information of the developers.")
            embed.add_field(name=f"{prefix}weather", value=f"The command you type for the bot to show you the current weather for the requested coordinates. **COORDINATES ONLY** Usage: {prefix}weather 60.3913 5.3221 Output: Bergen, Vestland, Norway Weather:")
            passed = 1
        if args == 'mod':
            embed.add_field(name=f"{prefix}kick", value="The command you type for the bot to kick the desired member **Must have permissions**")
            embed.add_field(name=f"{prefix}ban", value="The command you type for the bot to ban the desired member **Must have permissions**")
            embed.add_field(name=f"{prefix}clear", value="The command you type for the bot to clear the desired number of messages. **Must have manage messages permissions**")
            passed = 1
        if args == 'platform':
            embed.add_field(name=f"{prefix}newposts", value="The command you type for the bot to show the newest posts from the platform! **Takes couple seconds, be patient**")
            embed.add_field(name=f"{prefix}checkpost", value="The command you type for the bot to check the post for the number you put! **Also takes couple seconds**")
            embed.add_field(name=f"{prefix}searchpost", value="The command you type for the bot to search posts on the platform!")
            passed = 1
        if args == 'translate':
            embed.add_field(name=f"{prefix}translateoptions", value=f"The command you type for the bot to show you the options for the {prefix}translate command.")
            embed.add_field(name=f"{prefix}translate", value=f"The command you type for the bot to translate followed by the language code (which can be found using {prefix}translateoptions command) and the content.")
            passed = 1
        if args == 'fun':
            embed.add_field(name=f"{prefix}hello", value="Bot will say Hello.", inline=True)
            embed.add_field(name=f"{prefix}say", value="The command you type followed by your desired message to make the bot say that. **Does not support DM**", inline=True)
            embed.add_field(name=f"{prefix}meme", value="The command you type for the bot to show a random meme from the list!")
            embed.add_field(name=f"{prefix}urban", value=f"The command you type for the bot to define the requested term! usage: {prefix}urban <term here>")
            passed = 1
        if args == 'misc':
            embed.add_field(name=f"{prefix}avatar", value="The command you type for the bot to show you or the user mention's avatar!")
            passed = 1
        if args == 'dev':
            embed.add_field(name=f"{prefix}devverify (Developer Only)", value=f"Usage: {prefix}devverify <DiscordID> <WalkerID>")
            embed.add_field(name=f"{prefix}devunverify (Developer Only)", value=f"Usage: {prefix}devunverify <DiscordID>")
            passed = 1
        member = ctx.author
        embed.set_footer(text="Noice")
        if passed == 1:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send(embed=embed)
            logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
            current_time = datetime.utcnow()
            embed1=discord.Embed(title=f"Log: help ({args})", color=0x0400ff)
            embed1.add_field(name="Action: Gethelp", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
            try:
                await logchannel.send(embed = embed1)
            except AttributeError:
                await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")
    except:
        print (traceback.format_exc())

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command(pass_context=True)
async def say(ctx, *, args):
    try:
        Content = args
        await ctx.message.delete()
        await ctx.channel.send(Content)
    except AttributeError:
        async with ctx.channel.typing():
            await asyncio.sleep(2)
            await ctx.channel.send("This command does not support DM.")
    except discord.errors.HTTPException:
        await ctx.channel.send(f"What are you making me say? include it after `{prefix}say`!")
    logchannel = discord.utils.get(ctx.author.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: say", color=0x0400ff)
    embed.add_field(name=f"Action: SayCommand({Content})", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {ctx.author.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 5, commands.BucketType.user)
@Bot.command()
async def go(ctx, args):
    WalkerID = {}
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    current_time = datetime.utcnow()
    DiscordID = member.id
    if args != '0':
        WalkerID[DiscordID] = args
    else:
        WalkerID[DiscordID] = '#0'
    if '#' in args:
        WalkerID[DiscordID] = args[1:]
    print(WalkerID[DiscordID])
    embed=discord.Embed(title="Log: go", color=0x0400ff)
    embed.add_field(name=f"Action: CommentCheck AttemptedID: {WalkerID[DiscordID]}", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except:
        pass
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("Thanks, I'm checking your comment.")
    try:
        response = comments([email, password], commenturl)
        lastComment = response[-1]
        walkerIDFound = lastComment[0]
        tokenFound = lastComment[1]
        print("1)" + tokenFound)
        issue = 0
        if lastComment == None or walkerIDFound == None or tokenFound == None:
            issue = 1
    except:
        issue = 1
    try:
        r = login([email, password], commenturl)
        print("2)" + Bot.commentToken[DiscordID])
        try:
            if walkerIDFound == WalkerID[DiscordID] and Bot.commentToken[DiscordID] in tokenFound:
                pass
            if walkerIDFound == WalkerID[DiscordID] and Bot.commentToken[DiscordID] in tokenFound:
                if str(r) == '<Response [401]>':
                    async with ctx.channel.typing():
                        await ctx.channel.send(f"Response 401 occured. Big problem.")
                if str(r) == '<Response [200]>':
                    await ctx.channel.send(f"Response 200, good.")
                else:
                    await ctx.channel.send(f"Response {str(r.status_code)}.")
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send("Verification completed, congrats!")
                role = get(member.guild.roles, name = verifiedrolename)
                unrole = get(member.guild.roles, name = unverifiedrolename)
                if WalkerID[DiscordID] != '#0':
                    WalkerIDnick = "#"+str(WalkerID[DiscordID])
                else:
                    WalkerIDnick = str(WalkerID[DiscordID])
                if '#' in args:
                    WalkerID[DiscordID] = args[1:]
                generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
                if str(list(mycol.find({'DiscordID': member.id},{'WalkerID'}))) != '[]':
                    async with ctx.channel.typing():
                        await asyncio.sleep(1)
                        await ctx.channel.send("The member is already verified, updating instead. Don't worry.")
                    mydict = {'WalkerID': int(WalkerID[DiscordID]), 'DiscordID': int(DiscordID)}
                    x = mycol.update_one({'DiscordID': int(DiscordID)},{'$set': {'WalkerID': int(WalkerID[DiscordID])}})
                    print(x)
                else:
                    mydict = {'WalkerID': int(WalkerID[DiscordID]), 'DiscordID': int(DiscordID)}
                    x = mycol.insert_one(mydict)
                    print(x)
                try:
                    await member.add_roles(role)
                    await member.remove_roles(unrole)
                    await member.edit(nick=WalkerIDnick)
                except discord.errors.Forbidden:
                    async with ctx.channel.typing():
                        await asyncio.sleep(1)
                        await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
                except:
                    pass
                if Bot.commentToken[DiscordID] == None:
                    async with ctx.channel.typing():
                        await asyncio.sleep(2)
                        await ctx.channel.send(f"You need to do the command {prefix}verify first. know that the Generated token works one time only.")
                else:
                    await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
                    Bot.commentToken[DiscordID] = None 
            else:
                issue = 1
        except UnboundLocalError:
            issue = 1
        if issue == 1:
            if str(r) == '<Response [200]>':
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(f"Continuing with backup method with Response 200.")
            else:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(f"Response {str(r.status_code)}.")
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("Didn't find your comment using the main method. Trying alternative method.")
            with req.urlopen(url) as response:
                data = json.load(response)
            commentCounter = 0
            commentAuthor = data[commentCounter]['author']
            try:
                commentAuthorName = int(data[commentCounter]['author_name'])
            except:
                pass
            tokenFound = data[commentCounter]['content']['rendered'][3:-5]
            print(f'commentAuthor: {commentAuthor}')
            print(f'commentAuthorName: {commentAuthorName}')
            print(f'keyEnter: {tokenFound}')
            print(f'TokenGenerated: {Bot.commentToken[DiscordID]}')
            if WalkerID[DiscordID] != '#0':
                if int(commentAuthorName) >= 50:
                    walkerIDFound = commentAuthorName
                else:
                    walkerIDFound = commentAuthor
            else:
                pass
            print(f'WalkerID: {walkerIDFound}')
            if walkerIDFound == int(WalkerID[DiscordID]) and Bot.commentToken[DiscordID] in tokenFound:
                pass
            if walkerIDFound == int(WalkerID[DiscordID]) and Bot.commentToken[DiscordID] in tokenFound:
                async with ctx.channel.typing():
                    await ctx.channel.send("Verification completed, congrats!")
                role = get(member.guild.roles, name = verifiedrolename)
                unrole = get(member.guild.roles, name = unverifiedrolename)
                if WalkerID[DiscordID] != '#0':
                    WalkerIDnick = "#"+str(WalkerID[DiscordID]) #added exception for alan lol
                else:
                    WalkerIDnick = WalkerID[DiscordID]
                generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
                if str(list(mycol.find({'DiscordID': member.id},{'WalkerID'}))) != '[]':
                    async with ctx.channel.typing():
                        await asyncio.sleep(1)
                        await ctx.channel.send("The member is already verified, updating instead. Don't worry.")
                    
                else:
                    mydict = { "WalkerID": int(WalkerID[DiscordID]), "DiscordID": int(DiscordID) }
                    x = mycol.insert_one(mydict)
                    print(x)
                try:
                    await member.add_roles(role)
                    await member.remove_roles(unrole)
                    await member.edit(nick=WalkerIDnick)
                except discord.errors.Forbidden:
                    async with ctx.channel.typing():
                        await asyncio.sleep(1)
                        await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
                    async with ctx.channel.typing():
                        await asyncio.sleep(1)
                        await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
                    Bot.commentToken[DiscordID] = None
            else:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send("Could not find your comment with every method, if you did comment, please make sure you commented the token below the link and you entered the correct Walker ID.")  
    except (KeyError, TypeError):
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(f"You need to do the command {prefix}verify first. know that the Generated token works one time only.")
    except AttributeError:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Make sure the permissions are setup right, channels and roles exist.")
            print(traceback.format_exc())
    except ValueError:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Invalid ID format.")
    except:
        print (traceback.format_exc())
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Unknown error.")
    print("3)" + walkerIDFound)
    print("4)" + WalkerID[DiscordID])



@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def unverify(ctx):
    member = ctx.author
    if str(list(mycol.find({'DiscordID': member.id},{'WalkerID'}))) != '[]':
        try:
            logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
            role = get(member.guild.roles, name = verifiedrolename)
            unrole = get(member.guild.roles, name = unverifiedrolename)
            await member.add_roles(unrole)
            await member.remove_roles(role)
        except:
            pass
        delete = mycol.delete_many({'DiscordID': ctx.author.id})
        try:
            delete = mycol.delete_many({'DiscordID': str(ctx.author.id)})
        except:
            pass
        print(delete)
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Unverified.")
        current_time = datetime.utcnow()
        embed=discord.Embed(title="Log: unverify", color=0x0400ff)
        embed.add_field(name="Action: unverify", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
        try:
            await logchannel.send(embed = embed)
        except AttributeError:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")
        except discord.errors.Forbidden:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            role = get(member.guild.roles, name = verifiedrolename)
            unrole = get(member.guild.roles, name = unverifiedrolename)
            await ctx.channel.send("Your not verified, but if you had the Walker role, I already removed it and added the unverified role. Please verify to use this command.")
            await member.add_roles(unrole)
            await member.remove_roles(role)

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
@has_permissions(administrator=True)
async def lastverified(ctx):
        x = mycol.find().sort([('_id', -1)]).limit(6)
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(str(list(x)))

@has_permissions(administrator=True)
@Bot.command()
async def forceverify(ctx, member: discord.Member, args):
    if str(list(mycol.find({'DiscordID': ctx.author.id},{'WalkerID'}))) != '[]':
        try:
            int(args)
            current_time = datetime.utcnow()
            WalkerID = {}
            role = get(member.guild.roles, name = verifiedrolename)
            unrole = get(member.guild.roles, name = unverifiedrolename)
            DiscordID = member.id
            logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
            WalkerID[DiscordID] = args
            generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
            try:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send("Verification completed, congrats! Note: Forceverify doesn't save the link to the database due to trust issues. Please tell them to verify manually in order to gain to access my commands and support for multi-server.")
                if WalkerID[DiscordID] != '#0':
                    WalkerIDnick = "#"+str(WalkerID[DiscordID])
                else:
                    WalkerIDnick = str(WalkerID[DiscordID])
                await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
                await member.add_roles(role)
                await member.remove_roles(unrole)
                await member.edit(nick=WalkerIDnick)
            except discord.errors.Forbidden:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {member.mention}'s nickname.")
            embed=discord.Embed(title=f"Log: forceverify {WalkerIDnick}", color=0x0400ff)
            embed.add_field(name="Action: forceverify", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
            try:
                await logchannel.send(embed = embed)
            except AttributeError:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")
        except ValueError:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("Invalid ID format.")
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Your not verified, please verify to use this command.")

@Bot.command()
async def devverify(ctx, arg1, arg2):
    DiscordIDdev = arg1
    WalkerIDdev = arg2
    try:
        if ctx.author.id in devids:
            if str(list(mycol.find({'DiscordID': int(DiscordIDdev)},{'WalkerID'}))) != '[]':
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send("Member already verified!"+ str(list(mycol.find({'DiscordID': int(DiscordIDdev)},{'WalkerID'}))))
                pass
            else:
                mydict = { "WalkerID": int(WalkerIDdev), "DiscordID": int(DiscordIDdev) }
                x = mycol.insert_one(mydict)
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(str(list(mycol.find({'DiscordID': DiscordIDdev},{'WalkerID'}))))
                    await ctx.channel.send(str(x))
    except ValueError:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("Invalid format!")

@Bot.command()
async def devunverify(ctx, args):
    DiscordIDdev = args
    try:
        if ctx.author.id in devids:
            if str(list(mycol.find({'DiscordID': int(DiscordIDdev)},{'WalkerID'}))) == '[]':
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send("Member already isn't verified!"+ str(list(mycol.find({'DiscordID': int(DiscordIDdev)},{'WalkerID'}))))
                pass
            else:
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(str(list(mycol.find({'DiscordID': int(DiscordIDdev)},{'WalkerID'}))))
                delete = mycol.delete_many({'DiscordID': int(DiscordIDdev)})
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(str(delete))
            try:
                delete = mycol.delete_many({'DiscordID': DiscordIDdev})
            except:
                pass
    except ValueError:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("Invalid format!")

@has_permissions(administrator=True)
@Bot.command()
async def forceunverify(ctx, member: discord.Member):
    if str(list(mycol.find({'DiscordID': ctx.author.id},{'WalkerID'})))!= '[]':
        current_time = datetime.utcnow()
        role = get(member.guild.roles, name = verifiedrolename)
        unrole = get(member.guild.roles, name = unverifiedrolename)
        logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
        try:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("Unverified.")
            await member.add_roles(unrole)
            await member.remove_roles(role)
        except discord.errors.Forbidden:
            await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
        embed=discord.Embed(title=f"Log: forceunverify", color=0x0400ff)
        embed.add_field(name="Action: forceunverify", value=f"**User**: {ctx.author.mention} **Time**: {current_time} UTC", inline=True)
        try:
            await logchannel.send(embed = embed)
        except AttributeError:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Your not verified, please verify to use this command.")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def newposts(ctx):
    if str(list(mycol.find({'DiscordID': ctx.author.id},{'WalkerID'}))) != '[]':
        embed = discord.Embed(title="Looking for new posts...")
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            message = await ctx.channel.send(embed=embed)
        embed = discord.Embed(title="Posts List")
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        posts = post([email,password], allposts)
        index = 0
        for i in posts:
            author = i[0]
            try:
                int(author)
                str(author)
                
                author = str(index) + ". #" + author
            except:
                author = str(index) + ". " + i[0]
            title = i[1]
            link = i[2]
            index+=1
            embed.add_field(name=author, value= f"[{title}]({link})", inline=True)
        await message.edit(embed=embed)
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Your not verified, please verify to use this command.")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def avatar(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(userAvatar)

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def checkpost(ctx, args):
    if str(list(mycol.find({'DiscordID': ctx.author.id},{'WalkerID'}))) != '[]':
        embed = discord.Embed(title="Checking post!", color=0x0400ff)
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            message = await ctx.channel.send(embed=embed)

        posts = post([email,password], allposts)
        try:
            length = int(args)
            if length > len(posts) or length < 0:
                print(length)
                embed = discord.Embed(title="Out of range!", color=0x0400ff)
                await message.edit(embed=embed)
            else:
                postURL = posts[length][2]
                desc = post_contents([email, password], postURL)
                author = posts[length][0]
                try:
                    int(author)
                    str(author)
                    author = "#" + author
                except:
                    pass
                title = author + " - " + posts[length][1]
                embed = discord.Embed(title=title, description=desc , color=0x0400ff)
                embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await message.edit(embed=embed)
        except:
            embed = discord.Embed(title="Error! please check if you wrote it right!", color=0x0400ff)
            await message.edit(embed=embed)
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Your not verified, please verify to use this command.")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, args=None):
    reason = args
    await member.kick(reason=reason)
    embed=discord.Embed(title="Kicked", description=f"**{member.mention}** has been kicked from the server by **{ctx.author.mention}**")
    embed.add_field(name="Reason", value=str(reason))
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(embed=embed)
    current_time = datetime.utcnow()
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    embed=discord.Embed(title=f"Log: kick ({ctx.author.name}#{ctx.author.discriminator})", color=0x0400ff)
    embed.add_field(name="Action: Kick member", value=f"**User**: {member.mention} **Admin/Mod**: {ctx.author.mention} **Time**: {current_time} UTC **Reason**: {reason}", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def searchpost(ctx, *, args):
    if str(list(mycol.find({'DiscordID': ctx.author.id},{'WalkerID'}))) != '[]':
        print(args)
        toSearch = args
        embed = discord.Embed(title="Searching posts...")
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            message = await ctx.channel.send(embed=embed)
        posts = searchPost([email,password], toSearch, max=20)
        embed = discord.Embed(title="Posts List")
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        index = 0
        for i in posts:
            author = i[0]
            try:
                int(author)
                str(author)
                
                author = str(index) + ". #" + author
            except:
                author = str(index) + ". " + i[0]
            title = i[1]
            link = i[2]
            index+=1
            embed.add_field(name=author, value= f"[{title}]({link})", inline=True)
        await message.edit(embed=embed)
    else:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Your not verified, please verify to use this command.")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None, *, args=None):
    #print (str(list(member.guild_permissions)))
    if member == None:
        embed=discord.Embed(title="Error", description=f"Who do you want to ban?")
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(embed = embed)
    reason = args
    if 'administrator' in list(member.guild_permissions):
        embed=discord.Embed(title="Error", description=f"You can't ban a moderator.")
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(embed = embed)
    print (member.guild_permissions)
    await member.ban(reason=reason)
    embed1=discord.Embed(title="Banned", description=f"**{member.mention}** has been banned from the server by **{ctx.author.mention}**")
    embed1.add_field(name="Reason", value=str(reason))
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(embed=embed1)
    current_time = datetime.utcnow()
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    embed2=discord.Embed(title=f"Log: ban ({member.name}#{member.discriminator})", color=0x0400ff)
    embed2.add_field(name="Action: Ban member", value=f"**User**: {member.mention} **Admin/Mod**: {ctx.author.mention} **Time**: {current_time} UTC **Reason**: {reason}", inline=True)
    try:
        await logchannel.send(embed = embed2)
    except AttributeError:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")
    except:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Insufficient permissions!")

#@commands.cooldown(1, 1, commands.BucketType.user)
#@Bot.command()
#@commands.has_permissions(ban_members=True)
#async def unban(ctx, *, member, args):
    #reason = args
    #banned_users = await ctx.guild.bans()
    #memberName, memberDiscriminator = member.split("#")
    #for ban_entry in banned_users:
        #user = ban_entry.user
        #if (user.name, user.discriminator) == (memberName, memberDiscriminator):
            #await ctx.guild.unban(user)
    #embed=discord.Embed(title="Unbanned", description=f"**{member.name}#{member.discriminator}** has been unbanned from the server by **{ctx.author.name}#{ctx.author.discriminator}**")
    #await ctx.channel.send(embed=embed)
    #current_time = datetime.utcnow()
    #logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    #embed=discord.Embed(title=f"Log: unban ({ctx.author.name}#{ctx.author.discriminator})", color=0x0400ff)
    #embed.add_field(name="Action: unban member", value=f"**User**: {member.name}#{member.discriminator} **Admin/Mod**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    #try:
        #await logchannel.send(embed = embed)
    #except AttributeError:
        #await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel {logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def urban(ctx, *, arg1):
    term = arg1
    async with ctx.channel.typing():
        try:
            await asyncio.sleep(1)
            r = requests.get(f"http://www.urbandictionary.com/define.php?term={term}")
            soup = BeautifulSoup(r.content, features="html5lib")
            send = soup.find("div",attrs={"class":"meaning"}).text
            embed = discord.Embed(title=term, color=0x0400ff)
            embed.add_field(name="Definition", value=send,inline=True)
            if len(embed) <=220:
                await ctx.channel.send(embed=embed)
            else:
                await ctx.channel.send("Character limit reached!")
        except AttributeError:
            await asyncio.sleep(1)
            embed = discord.Embed(title=term, color=0x0400ff)
            embed.add_field(name="Definition", value='No definitions found!',inline=True)
            await ctx.channel.send(embed=embed)

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def weather(ctx, arg1, arg2):
    Embed = discord.Embed(title="Getting weather information.")
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        message = await ctx.channel.send(embed=Embed)
    xcoor = arg1
    ycoor = arg2
    r = requests.get(f"https://weather.com/weather/today/l/{xcoor},{ycoor}")
    soup = BeautifulSoup(r.content, features="html5lib")
    send = soup.find("h1",attrs={"class":"CurrentConditions--location--1Ayv3"})
    send1 = soup.find("span",attrs={"class":"CurrentConditions--tempValue--3KcTQ"})
    send2 = soup.find("div",attrs={"class":"CurrentConditions--phraseValue--2xXSr"})
    send3 = soup.find("h2",attrs={"class":"AlertHeadline--alertText--aPVO9"})
    try:
        Celcius = round((int(send1.text[:-1]) - 32) * 5/9)
        if send3 == None:
            Embed = discord.Embed(title="Weather",color=0x0400ff)
            Embed.add_field(name = "Requested weather", value=f"**{send.text}**: {send1.text} Farenheit, {str(Celcius)}° Celcius. {send2.text}")
        else:
            Embed = discord.Embed(title="Weather",color=0x0400ff)
            Embed.add_field(name = "Requested weather", value=f"**{send.text}**: {send1.text} Farenheit, {str(Celcius)}° Celcius. {send2.text}. Main Alert: {send3.text}")
        await message.edit(embed=Embed)
    except AttributeError:
        await ctx.channel.edit("No data avaliable for the requested location!")
    except:
        print (traceback.format_exc())

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def twitter(ctx, args):
    user = args
    r = requests.get(f"https://twitter.com/{user}/")
    soup = BeautifulSoup(r.content, features="html5lib")
    soup.findAll(text=True)
    print(soup)

@commands.cooldown(1, 1, commands.BucketType.user)
@Bot.command()
async def meme(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(random.choice(memelisthaha))

@Bot.command()
async def sourcecode(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("here's the code! https://github.com/junyuxu2006/walkerverificationbot/")

@Bot.command()
async def about(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("This bot is the ONLY Open-source, it has support for ALL Walker IDs, and multi-server compatible. This Walker verification bot is developed by Walker #7416 and Walker #34860. It works in Walker Discord servers.")

@Bot.command()
async def servercount(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(f"I'm in {str(len(Bot.guilds)) } servers!")

@Bot.command()
async def serverinvite(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("Invite for the Green Nexus Walker verification bot official server: https://discord.gg/ZrK2m3q")

@Bot.command()
async def donate(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=SQA2T7K5ACTPJ&item_name=GreenNexusBotSupport&currency_code=USD&source=url")

@Bot.command()
async def vote(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("https://top.gg/bot/753420267602313347 Vote me on top.gg through this link!")

@Bot.command()
async def website(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("https://greennexus.junyuxu.com/index")

@Bot.command()
async def ping(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(f"ping: {round(Bot.latency * 1000)} ms")

@Bot.command()
async def usercount(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(f"I currently have {mycol.count_documents({})} Walker Discord accounts verified!")

@Bot.command()
async def contact(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(f"Contact us by joining our discord server! Just simply type {prefix}serverinvite.")

@Bot.command()
async def translateoptions(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send("Here is a full list of languages and the usage! for example: no is Norwegian! https://docs.google.com/document/d/1T3qfI2o73FEkfUfd6oM21fFg4E0Gq97Czk6hCIkC0WU/edit?usp=sharing")
@Bot.command()
async def translate(ctx, arg1, *, args):
    language = arg1
    data = args 
    translator = Translator()
    dt1 = translator.detect(data)
    translated = translator.translate(data, src=dt1.lang, dest=language)
    async with ctx.channel.typing():
        await asyncio.sleep(1)
        await ctx.channel.send(translated.text)

@commands.has_permissions(manage_messages=True)
@commands.cooldown(5, 5, commands.BucketType.user)
@Bot.command()
async def clear(ctx, args):
    current_time = datetime.utcnow()
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    try:
        clearnumber = 0
        if int(args) <= 200:
            clearnumber = int(args)
            await ctx.message.channel.purge(limit = 1)
            await ctx.message.channel.purge(limit = clearnumber)
            if int(args) == 1:
                embed = discord.Embed(title=f"I have deleted {args} message", color=0x0400ff)
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(embed=embed, delete_after = 1)
            else:
                embed = discord.Embed(title=f"I have deleted {args} messages", color=0x0400ff)
                async with ctx.channel.typing():
                    await asyncio.sleep(1)
                    await ctx.channel.send(embed=embed, delete_after = 1)
        else:
            async with ctx.channel.typing():
                await asyncio.sleep(1)
                await ctx.channel.send("The limit is 200 messages.")
    except ValueError:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("Please put a valid number lol.")
    except discord.errors.Forbidden:
        async with ctx.channel.typing():
            await asyncio.sleep(1)
            await ctx.channel.send("I don't have enough permissions :(")
    except:
        print (traceback.format_exc())
    embedlol=discord.Embed(title=f"Log: Clear ({member.name}#{member.discriminator})", color=0x0400ff)
    if int(args) == 1:
        embedlol.add_field(name=f"Action: {args} message cleared", value=f"**Member**: {member.mention} **Time**: {current_time} UTC",inline=True)
    else:
        embedlol.add_field(name=f"Action: {args} messages cleared", value=f"**Member**: {member.mention} **Time**: {current_time} UTC",inline=True)
    try:
        await logchannel.send(embed=embedlol)
    except AttributeError:
        pass
    except:
        print (traceback.format_exc())
        pass


@Bot.event
async def on_guild_join(guild):
    await random.choice(guild.text_channels).send(f'{guild.owner.mention} Thanks for adding me. In order for me to properly function, make sure you have a role named "{verifiedrolename}" and "{unverifiedrolename}", and make sure my role is above them. Your server must have channels that I can send messages that are named {verificationchannelname}, {logchannelname}, and {generalchannelname}.')

@Bot.event
async def on_member_join(member):
    current_time = datetime.utcnow()
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    embed=discord.Embed(title=f"Log: join ({member.name}#{member.discriminator})", color=0x0400ff)
    embed.add_field(name="Action: Member joined", value=f"**Member**: {member.mention} **Time**: {current_time} UTC",inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        pass
    try:
        channel = discord.utils.get(member.guild.text_channels, name = verificationchannelname)
        result = mycol.find({'DiscordID': member.id},{'WalkerID'}) 
        strlistitem = str(list(result))
        if strlistitem != '[]':
            try:
                result = mycol.find({'DiscordID': member.id},{'WalkerID'})
                result = list(result)[0]['WalkerID']
                intWalkerID = int(result)
                role = get(member.guild.roles, name = verifiedrolename)
                await member.add_roles(role)
                WalkerIDnick = '#' + str(intWalkerID)
                await member.edit(nick=WalkerIDnick)
                generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
                await generalchannel.send(f"Walker {WalkerIDnick} has joined, Welcome!")
                current_time = datetime.utcnow()
                embed=discord.Embed(title=f"Log: autoverified, we know that the member is an walker. ({member.name}#{member.discriminator})", color=0x0400ff)
                embed.add_field(name="Action: Member autoverified", value=f"**Member**: {member.mention} **Time**: {current_time} UTC **WalkerID**: {WalkerIDnick}",inline=True)
                try:
                    await logchannel.send(embed = embed)
                except AttributeError:
                    pass
            except discord.errors.Forbidden:
                await random.choice(member.guild.text_channels).send(f"{member.guild.owner.mention} I do not have permissions to add/remove roles and/or change {member.mention}'s nickname.")
            except ValueError:
                channel.send('A error occured, please unverify, then verify.')
            except:
                pass
        else:
            unrole = get(member.guild.roles, name = unverifiedrolename)
            await member.add_roles(unrole)
            await channel.send(f"Welcome{member.mention}. **{member.guild.name}** is a server dedicated to Walkers with an official ID. I'm your friendly verification bot to help you to authorize yourself, getting access to all the Walkers channels on this server in return, please type `{prefix}verify` to get started on your verification process.")
    except AttributeError:
        await random.choice(member.guild.text_channels).send(f"{member.guild.owner.mention}, the roles are not setup correctly, please fix it.")

@Bot.event
async def on_member_remove(member):
    current_time = datetime.utcnow()
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    embed=discord.Embed(title=f"Log: Leave ({member.name}#{member.discriminator})", color=0x0400ff)
    embed.add_field(name="Action: Member left", value=f"**Member**: {member.mention} **Time**: {current_time} UTC",inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        pass

class TopGG(commands.Cog):
    """
    This example uses dblpy's autopost feature to post guild count to top.gg every 30 minutes.
    """

    def __init__(self, bot):
        self.bot = bot
        self.token = topggtoken  # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  # Autopost will post your guild count every 30 minutes
    @commands.Cog.listener()
    async def on_guild_post(self):
        print("Server count posted successfully")

def setup(bot):
    bot.add_cog(TopGG(bot))


Bot.run(token)
