# Making a Discord "App"
Before we start coding, we need to make a discord app using the [discord developer portal](https://discord.com/developers/applications). 
You need to create a discord app by pressing "new application" and then adding a bot to that application.
Discord has a full [tutorial](https://discordpy.readthedocs.io/en/latest/discord.html) for this process.

## Client ID and Bot Token
Our application will contain a unique **client ID** which we will need when creating the bot, as the name suggestes it will identify our client application as a client application. This id will be used to in our bot's invite link when its time to invite it to our server.
**The bot token** is used to identify the bot. Every bot has its own token, this token should never be revealed to anyone except the bot's developers.

## Bot Version Guide
#### Updates will be added via different branches

Version 1:
-Ability to reply to messages with messages

Version 2:
-Ability to send images as replies

Version 3:
-Command features

Version 4:
-More commands added and choice between message replies and image replies