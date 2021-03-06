'''
Program: Star Wars Bot
Version: 2.0
Author: Adam Wahba
Date: 2021-03-06

Description:
This is the second version of the Star Wars Bot program.
The bot token has been removed in the public version of this program.

Functionality(VERSION 2):
This version of the bot has image sending/reply capability

OOP:
It is helpful to know what Object Oriented programming is before diving into the code of a discord bot.
There are many custom classes created by the discord developers such as the client class, bot class and message class. 
If you do not have any knowledge of OPP here is a link to an OPP in Python guide http://openbookproject.net/thinkcs/python/english3e/classes_and_objects_I.html

Decorators:
Discord.py requires the use of many decorators, knowledge of how decorators work and whet they do to functions would also be useful before attempting a project like this.
Discord.py only uses decorators to "register" functions so knowing when and where to use them will suffice. 
It can be a confusing topic so tread carefully and dont worry if you dont understand them fully because you can still follow along if you do not.
I will explain when and why they are used when they show up in this program. 
But for you curious coders out there, here are some links; 
https://medium.com/@cantsayihave/decorators-in-discord-py-e44ce3a1aae5
https://www.datacamp.com/community/tutorials/decorators-python

Discord client object:
The client object in the discord.py module represents our real bot client and is a very important object with many methods and features. 
Refer to this link for more information https://discordpy.readthedocs.io/en/latest/api.html#client

Note:
Make sure to have the discord API docs on-hand for reference as you go through the code
I will be using the API docs' own function descriptions in each function docstring. 
All of my own comments and descriptions will be found throughout the code.

Links and such;
Bot invite code: https://discord.com/api/oauth2/authorize?client_id=817142261304786947&permissions=0&scope=bot
'''

# The first thing we will need to do is import the discord module
import discord
from discord import *



# Bot Token and Client object
token = 'bot token goes here'  
client = discord.Client()   

# Most of the previous comments have been removed in this version for the sake of a cleaner looking prorgam file
# Comments in this file will be reserved for new methods that are not documented in the previous version

@client.event 
async def on_ready():  
    '''
    Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up.
    '''
    print('The force has awoken')
    

@client.event   
async def on_message(message):
    '''
    Called when a Message is created and sent.
    '''

    if 'hello there' in message.content.lower():
        await message.channel.send('General Kenobi')
   
    if 'blind' in message.content.lower() and message.author.id != client.user.id:
        await message.channel.send('So love has blinded you?')

    if 'high' and 'ground' in message.content.lower() and message.author.id != client.user.id:
        await message.channel.send('I have the high ground Anakin')
    
    if 'try' in message.content.lower() and message.author.id != client.user.id:
        await message.channel.send('Do or do not, there is no try.')










# Client run method
client.run(token)