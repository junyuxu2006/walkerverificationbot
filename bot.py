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
PATH = configs['PATH']
link = configs['link']
email = configs['email']
password = configs['password']
verifiedrolename = configs['verifiedrolename']
unverifiedrolename = configs['unverifiedrolename']
Invitelink = configs['Invitelink']



client = discord.Client()
commenturl = configs['commenturl']
token = configs['token']
verifiedrole = configs['verifiedrolename']
controlchannelname = configs['controlchannelname']
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



client.commentToken = ""
@client.event
async def on_message(message):
    member = message.author
    DiscordID = member.id
    if message.content.startswith("$verify"):
        token = hex(DiscordID)[2:]
        client.commentToken = token[:8] + secrets.token_urlsafe(6) + token[8:]
        stringToken = str(client.commentToken)
        await message.channel.send("NOTE: This discord bot is **still in development, if you experience errors, please contact Walker #7416.** Please make a comment on the following post exactly as the token below. Then, type `$go WalkerID(NO #)`, where WalkerID is YOUR OWN WALKER ID."+" <"+str(commenturl) + "> ")
        await message.channel.send("copy the token below and paste it in the comments section of the post.")
        await message.channel.send(stringToken)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello.')
    if message.content.startswith('$invite'):
        await message.channel.send("Invite me here! <"+Invitelink+">")
    if message.content.startswith('$help'):
        await message.channel.send("`$help` - list all the commands.")
        await message.channel.send("`$invite` - Invite link for the bot.")
        await message.channel.send("`$hello` - Bot will say Hello.")
        await message.channel.send("`$verify` - Shows instructions for verification, and generates a token to comment on.")
        await message.channel.send("`$go` - The command you type followed by your Walker ID for comment checking purposes.")
        await message.channel.send("`$ungo` - The command you type to unverify.")
    if message.content.startswith("$go "):
        await message.channel.send("Thanks, I'm checking your comment.")
        driver = webdriver.Chrome(PATH)
        driver.get(link)
        print(driver.title)
        inputemail = driver.find_element_by_id("user_login")
        inputemail.send_keys(email)
        inputpassword = driver.find_element_by_id("user_pass")
        inputpassword.send_keys(password)
        inputpassword.send_keys(Keys.ENTER)
        WalkerID = message.content[4:]
        print(WalkerID)
        #xpathWalkerID = str("//*[contains(text(), '"+WalkerID+"'"+")]")
        #xpathToken = str("//*[contains(text(), '"+client.commentToken+"'"+")]")
        WalkerIDelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/div[1]/a/span")
        #driver.find_elements_by_class_name("wid")
        Tokenelement = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/main/section/ul/li[last()]/div/p")
        #driver.find_elements_by_class_name("comment-author vcard")
        WalkerIDFound = WalkerIDelement.get_attribute('textContent')
        TokenFound = Tokenelement.get_attribute('textContent')
        await message.channel.send("Found ID: "+WalkerIDFound)
        time.sleep(1)
        await message.channel.send("Found Token: "+TokenFound)
        time.sleep(1)
        await message.channel.send("Entered ID: "+WalkerID)
        time.sleep(1)
        await message.channel.send("Generated Token: "+client.commentToken)
        time.sleep(1)
    if message.content.startswith('$ungo'):
        role = get(member.guild.roles, name = verifiedrolename)
        unrole = get(member.guild.roles, name = unverifiedrolename)
        await member.add_roles(unrole)
        await member.remove_roles(role)
        await message.channel.send("Unverified.")
    if TokenFound == client.commentToken and WalkerIDFound == WalkerID:
        time.sleep(2)
        await message.channel.send("Verified.")
        driver.quit()
        role = get(member.guild.roles, name = verifiedrolename)
        unrole = get(member.guild.roles, name = unverifiedrolename)
        await member.add_roles(role)
        await member.remove_roles(unrole)
        WalkerIDnick = "#"+WalkerID
        await member.edit(nick=WalkerIDnick)
        print(DiscordID)  
    else:
        time.sleep(2)
        await message.channel.send("Could not find your comment, if you did comment, please make sure you commented the token in the black box below the link and you entered the correct Walker ID.")
        driver.quit()
@client.event
async def on_guild_join(guild):
    await random.choice(guild.text_channels).send('Thanks for adding me. In order for me to properly function, make sure you have a role named "'+verifiedrolename+'" and "'+unverifiedrolename+'". My role has to be above them.')
client.run(token)
