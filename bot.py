from selenium import webdriver
from config import configs
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import discord
import secrets
import time
from discord.ext.commands import Bot
from discord.ext.commands import Cog
from discord.ext.commands import command
import random
from config import configs
from discord.ext import commands
from discord.utils import get
import asyncio
PATH = configs['PATH']
link = configs['link']
email = configs['email']
password = configs['password']
verifiedrolename = configs['verifiedrolename']
unverifiedrolename = configs['unverifiedrolename']
Invitelink = configs['Invitelink']
prefix = configs['prefix']
verificationchannelname = configs['verificationchannelname']

client = commands.Bot(command_prefix = prefix)
commenturl = configs['commenturl']
token = configs['token']
verifiedrole = configs['verifiedrolename']
controlchannelname = configs['controlchannelname']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.remove_command('help')
client.commentToken = ""
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
    await ctx.channel.send("NOTE: This discord bot is **still in development, if you experience errors, please contact Walker #7416.** Please make a comment on the following post exactly as the token below. Then, type `$go WalkerID(NO #)`, where WalkerID is YOUR OWN WALKER ID."+" <"+str(commenturl) + "> ")
    await ctx.channel.send("copy the token below and paste it in the comments section of the post.")
    await ctx.channel.send(stringToken)

@commands.cooldown(1, 30, commands.BucketType.user)
@client.command()
async def hello(ctx):
        await ctx.channel.send('Hello.')

@commands.cooldown(1, 30, commands.BucketType.user)
@client.command()
async def invite(ctx):
        await ctx.channel.send("Invite me here! <"+Invitelink+">")

@client.command()
async def help(ctx):
        embed=discord.Embed(title="Help", color=0x0400ff)
        embed.add_field(name="$help", value="shows this message.", inline=True)
        embed.add_field(name="$invite", value="Invite link for the bot.", inline=True)
        embed.add_field(name="$hello", value="Bot will say Hello.", inline=True)
        embed.add_field(name="$verify", value="Shows instructions for verification, and generates a token to comment on.", inline=True)
        embed.add_field(name="$go", value="The command you type followed by your Walker ID for comment checking purposes.", inline=True)
        embed.add_field(name="$ungo", value="The command you type to unverify.", inline=True)
        embed.add_field(name="$say", value="The command you type followed by your desired message to make the bot say that.", inline=True)
        embed.set_footer(text="Noice")
        await ctx.channel.send(embed=embed)
WalkerIDFound = {}
TokenFound = {}
@client.command()
async def say (ctx):
    try:
        Content = ctx.message.content[5:]
        await ctx.message.channel.purge(limit = 1)
        await ctx.channel.send(Content)
    except AttributeError:
        await ctx.channel.send("This command does not support DM.")
@client.command()
async def go (ctx):
        member = ctx.author
        DiscordID = member.id
        WalkerID = {}
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
        WalkerIDelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/div[1]/a/span")
        #driver.find_elements_by_class_name("wid")
        Tokenelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/p")
        #driver.find_elements_by_class_name("comment-author vcard")
        WalkerIDFound = {}
        TokenFound = {}
        WalkerIDFound[DiscordID] = WalkerIDelement.get_attribute('textContent')
        TokenFound[DiscordID] = Tokenelement.get_attribute('textContent')
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
            try:
                await member.add_roles(role)
                await member.remove_roles(unrole)
                await member.edit(nick=WalkerIDnick)
            except discord.errors.Forbidden:
                await ctx.channel.send("I do not have permissions to add/remove roles and/or change your nickname, please contact your Admin or owner.")
            print(DiscordID)  
        else:
            await asyncio.sleep(2)
            await ctx.channel.send("Could not find your comment, if you did comment, please make sure you commented the token in the black box below the link and you entered the correct Walker ID.")
            driver.quit()
@commands.cooldown(1, 30, commands.BucketType.user)
@client.command()
async def ungo(ctx):
        member = ctx.author
        role = get(member.guild.roles, name = verifiedrolename)
        unrole = get(member.guild.roles, name = unverifiedrolename)
        await member.add_roles(unrole)
        await member.remove_roles(role)
        await ctx.channel.send("Unverified.")


@client.event
async def on_guild_join(guild):
    await random.choice(guild.text_channels).send('Thanks for adding me. In order for me to properly function, make sure you have a role named "'+verifiedrolename+'" and "'+unverifiedrolename+'", and make sure my role is above them. Your server must have a public channel which I can send messages that is named "'+verificationchannelname+'.')
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
