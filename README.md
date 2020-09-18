# walkerverificationbot
Discord verification bot for Alan Walker's secret platform

To setup, make sure you have a role in your server named "Walker" and another one named "Unverified".
go to config.py, put the corresponding information like 'commenturl' is the url displayed for $verify command for commenting.
'email' field is the email for the account you have on the platform.
'password' field is the password for the account you have on the platform.
'invitelink' is the invite link for the bot (you can get it on Discord Developer Portal).
'PATH' is the path to your selenium web driver, please replace \ with double \ in 'PATH'.
'controlroomID' is the channel ID for the channel for managing the bot.
'controlchannelname' is the channel name for the control channel.
'unverifiedrolename' is the name of the unverified role.
'verifiedrolename' is the name of the verified role.
'link' is https://(DOMAIN NAME HERE)/wp-login.php?redirect_to=(POST LINK HERE)
'token' is your Discord bot token.

You need to install python 3.6 or above.
dependencies: discord, discord.py, selenium, time, secrets, mongodb, and pymongo.

Known issues: 
1. sometimes, the site requires a prove your humanity captcha (This will be fixed and the captcha will be done automatically)
