from selenium import webdriver
from config import configs
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
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

PATH = configs['PATH']
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

client.remove_command('help')
client.commentToken = ""

WalkerIDFound = {}
TokenFound = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    loggedin = 1
    while (loggedin == 1):
        activity = discord.Game(name="$help | We Are Unity", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="$help | Walkers are best friends", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="$help | Stop hater Walkers", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="$help | Maintain Peace and Unity", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name="$help | Stop Separatism", type=3)
        await client.change_presence(activity=activity)
        await asyncio.sleep(10)

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
    await ctx.channel.send("NOTE: This discord bot is **still in development, if you experience errors, please contact Walker #7416.** Please make a comment on the following post exactly as the token below. Then, type `$go WalkerID(NO #)`, where WalkerID is YOUR OWN WALKER ID. **IF the bot doesn't respond in 10 seconds to the command `$go`, there is a problem and you should contact #7416, if it takes a bit longer to respond, then that's completely normal.**"+" <"+str(commenturl) + "> ")
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
    embed.add_field(name="$help", value="shows this message.", inline=True)
    embed.add_field(name="$invite", value="Invite link for the bot.", inline=True)
    embed.add_field(name="$hello", value="Bot will say Hello.", inline=True)
    embed.add_field(name="$verify", value="Shows instructions for verification, and generates a token to comment on.", inline=True)
    embed.add_field(name="$go", value="The command you type followed by your Walker ID for comment checking purposes.", inline=True)
    embed.add_field(name="$ungo", value="The command you type to unverify.", inline=True)
    embed.add_field(name="$say", value="The command you type followed by your desired message to make the bot say that.", inline=True)
    embed.add_field(name="$lastverified", value="The command you type to show the last couple users with the user ID and Walker ID, **Admins only**", inline=True)
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
        await ctx.channel.send("What are you making me say? include it after `$say`!")
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
async def go(ctx):
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
    DiscordID = member.id
    WalkerID[DiscordID] = ctx.message.content[4:]
    await ctx.channel.send("Thanks, I'm checking your comment.")
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    print(driver.title)
    inputemail = driver.find_element_by_id("user_login")
    inputemail.send_keys(email)
    inputpassword = driver.find_element_by_id("user_pass")
    inputpassword.send_keys(password)
    inputpassword.send_keys(Keys.ENTER)
    WalkerID[DiscordID] = ctx.message.content[4:]
    print(WalkerID[DiscordID])
    #xpathWalkerID = str("//*[contains(text(), '"+WalkerID+"'"+")]")
    #xpathToken = str("//*[contains(text(), '"+client.commentToken+"'"+")]")
    try:
        WalkerIDelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/div[1]/a/span")
        #driver.find_elements_by_class_name("wid")
        Tokenelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/p")
        #driver.find_elements_by_class_name("comment-author vcard")
        WalkerIDFound = {}
        TokenFound = {}
        WalkerIDFound[DiscordID] = WalkerIDelement.get_attribute('textContent')
        TokenFound[DiscordID] = Tokenelement.get_attribute('textContent')
        try:
            TokenFound[DiscordID] = Tokenelement.get_attribute('textContent')
            if TokenFound[DiscordID] == client.commentToken[DiscordID] and WalkerIDFound[DiscordID] == str(WalkerID[DiscordID]):
                await ctx.channel.send("Verified.")
                driver.quit()
                role = get(member.guild.roles, name = verifiedrolename)
                unrole = get(member.guild.roles, name = unverifiedrolename)
                WalkerIDnick = "#"+str(WalkerID[DiscordID])
                WalkerIDdict = {"walkerID": WalkerID}
                generalchannel= discord.utils.get(member.guild.text_channels, name = generalchannelname)
                with open ('data.json','r+') as f:
                    json.dump(WalkerIDdict, f)
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
                await asyncio.sleep(2)
                await ctx.channel.send("Could not find your comment, if you did comment, please make sure you commented the token below the link and you entered the correct Walker ID.")
                driver.quit()
        except KeyError:
            await ctx.channel.send("An error occured, try again now with `$verify`. This is most likely caused by someone running this command on this bot at the same time as you.")
            driver.quit()
        except selenium.common.exceptions.NoSuchElementException:
            await ctx.channel.send("An error occured. You may have to wait a while for this error to be fixed, but in most cases, trying again with `$verify` will fix the problem.")
            driver.quit()
        except IndexError:
            await ctx.channel.send("An error occured, try again now with `$verify`, then `$go`. This is most likely caused by you trying to put a text, nothing after, unmatched ID, or your Walker ID with the # without running `$verify`, which is invalid, retrying with the correct usage might fix the problem.")
            driver.quit()
    except selenium.common.exceptions.NoSuchElementException:
        captchaquestion = driver.find_element_by_xpath("/html/body/div/form/div/span").get_attribute('textContent')
        captchaquestion = captchaquestion.strip("   ")
        captchaquestionnumberlist = captchaquestion.split('+')
        captchaanswer = captchaquestionnumberlist[0] + captchaquestionnumberlist[1]
        cinputelement = driver.find_element_by_xpath("/html/body/div/form/div/input[1]")
        cinputelement.send_keys(captchaanswer)
        cinputelement.send_keys(Keys.ENTER)
        inputemail.send_keys(email)
        inputpassword.send_keys(password)
        inputpassword.send_keys(Keys.ENTER)
        driver.get(link)
        WalkerIDelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/div[1]/a/span")
        #driver.find_elements_by_class_name("wid")
        Tokenelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/p")
        #driver.find_elements_by_class_name("comment-author vcard")
        WalkerIDFound = {}
        TokenFound = {}
        WalkerIDFound[DiscordID] = WalkerIDelement.get_attribute('textContent')
        TokenFound[DiscordID] = Tokenelement.get_attribute('textContent')
        try:
            await ctx.channel.send("Found ID: "+WalkerIDFound[DiscordID])
            await asyncio.sleep(1)
            await ctx.channel.send("Found Token: "+TokenFound[DiscordID])
            await asyncio.sleep(1)
            await ctx.channel.send("Entered ID: "+WalkerID[DiscordID])
            await asyncio.sleep(1)
            await ctx.channel.send("Generated Token: "+client.commentToken[DiscordID])
            await asyncio.sleep(1)
            TokenFound[DiscordID] = Tokenelement.get_attribute('textContent')
            if TokenFound[DiscordID] == client.commentToken[DiscordID] and WalkerIDFound[DiscordID] == str(WalkerID[DiscordID]):
                await asyncio.sleep(2)
                await ctx.channel.send("Verified.")
                driver.quit()
                role = get(member.guild.roles, name = verifiedrolename)
                unrole = get(member.guild.roles, name = unverifiedrolename)
                WalkerIDnick = "#"+str(WalkerID[DiscordID])
                with open ('data.walkerdata','a') as f:
                    f.write(str(WalkerID))
                try:
                    await member.add_roles(role)
                    await member.remove_roles(unrole)
                    await member.edit(nick=WalkerIDnick)
                except discord.errors.Forbidden:
                    await ctx.channel.send(f"{ctx.author.guild.owner.mention} I do not have permissions to add/remove roles and/or change {ctx.author.mention}'s nickname.")
                print(DiscordID)  
            else:
                await asyncio.sleep(2)
                await ctx.channel.send("Could not find your comment, if you did comment, please make sure you commented the token in the black box below the link and you entered the correct Walker ID.")
                driver.quit()
        except KeyError:
            await ctx.channel.send("An error occured, try again now with `$verify`. This is most likely caused by someone running this command on this bot at the same time as you.")
            driver.quit()
        except selenium.common.exceptions.NoSuchElementException:
            await ctx.channel.send("An error occured. You may have to wait a while for this error to be fixed, but in most cases, trying again with `$verify` will fix the problem.")
            driver.quit()
        except IndexError:
            await ctx.channel.send("An error occured, try again now with `$verify`, then `$go`. This is most likely caused by you trying to put a text, nothing after, unmatched ID, or your Walker ID with the # without running `$verify`, which is invalid, retrying with the correct usage might fix the problem.")
            driver.quit()
@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
async def ungo(ctx):
    member = ctx.author
    logchannel = discord.utils.get(member.guild.text_channels, name = logchannelname)
    role = get(member.guild.roles, name = verifiedrolename)
    unrole = get(member.guild.roles, name = unverifiedrolename)
    await member.add_roles(unrole)
    await member.remove_roles(role)
    await ctx.channel.send("Unverified.")
    current_time = datetime.utcnow()
    embed=discord.Embed(title="Log: ungo", color=0x0400ff)
    embed.add_field(name="Action: unverify", value=f"**User**: {ctx.author.name}#{ctx.author.discriminator} **Time**: {current_time} UTC", inline=True)
    try:
        await logchannel.send(embed = embed)
    except AttributeError:
        await ctx.channel.send(f"Unable to log this action, {member.guild.owner.mention}. Does the channel #{logchannelname} exist?")

@commands.cooldown(1, 1, commands.BucketType.user)
@client.command()
@has_permissions(administrator=True)
async def lastverified(ctx):
    with open ('data.json','r') as f:
        content = json.load(f)
        await ctx.channel.send(content["walkerID"])

@client.event
async def on_guild_join(guild):
    await random.choice(guild.text_channels).send(f'{guild.owner.mention} Thanks for adding me. In order for me to properly function, make sure you have a role named "{verifiedrolename}" and "{unverifiedrolename}", and make sure my role is above them. Your server must have a channel  that I can send messages that is named {verificationchannelname}, {logchannelname}, and {generalchannelname}.')

@client.event
async def on_member_join(member):
    unrole = get(member.guild.roles, name = unverifiedrolename)
    channel = discord.utils.get(member.guild.text_channels, name = verificationchannelname)
    await member.add_roles(unrole)
    try:
        await channel.send(f"Hey {member.mention}, welcome to **{member.guild.name}**, please type `$verify` to get started on your verification process.")
    except AttributeError:
        await random.choice(member.guild.text_channels).send(f"Hey {member.mention}, welcome to **{member.guild.name}**, please type `$verify` to get started on your verification process.")
client.run(token)
