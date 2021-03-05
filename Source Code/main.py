'''
Author: Adam Wahba
Date: 2021-03-04

Description:
This is the main bot program's source code.
The bot token has been removed in the public version of this program.

Functionality:
This bot will not have commands functionality. As in, there will be no custom commands that may be used with this bot.
A version of this bot with command functionality may be added in the future.

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



# Now I will create a variable to store my bot token as well as instantiate or "construct" a client object 
token = 'bot token goes here'  
client = discord.Client()   


# Now we can add some functions to our bot. 


# Discord has many built-in functions which are automatically called when certain things happen. These things are called events.
# Much like in other modules, such as pygame. Events will trigger these functions. 


# This is an instance when we would need to use one of the discord.py decorators
# Here we use the @Client.event decorator to register this function.
# It will be called when a certain event triggers it to be called.
# In this case, it will be called when the bot is ready and online. 
@client.event 
async def on_ready():   # Notice the async syntax; all functions of this bot will be using it. async/await will not be explained in the code to avoid extra clutter. External explinations will be linked. 
    '''
    Called when the client is done preparing the data received from Discord. Usually after login is successful and the Client.guilds and co. are filled up.
    '''
    # I will have the bot send a simple message to console when it is ready to go.
    print('The force has awoken')
    # There is no need to add use the await syntax just yet

# Awesome, now the bot will print this message to console after it runs.
# Now we can add some basic functionality, such as the ability to reply to messages.
# We will have the bot reply to messages containing keywords, keeping with the star wars theme of the bot. I will have it reply to certain quotes from star wars


# First we need to set up another function, this time it will be called whenever the 'on_message' event is triggered
# It is triggered whenever a message is sent to a discord channel that the bot can see. 
# We can code the bot listen to only listen to certain channels, certain users and add many other restrictions. For this example I will keep it general to any user and any channel

@client.event   # Once again we use the decorator to register the function
async def on_message(message):
    '''
    Called when a Message is created and sent.
    '''
    # This function will reply to a few key phrases
    # These phrases will not be cases sensitive.
    # Some of the phrases will require some code to avoid a spam reply bug; will explain below

    # I will not use elif statements in this function because I want the bot to be able to reply in full if all of these keywords are present in a single message 

    if 'hello there' in message.content.lower():
        # This statement will check if the phrase 'hello there' is in whatever message has been sent. 
        # The message is formatted to lowercase so this condition is true so long as the letters within the substring "HELLO THERE' are present within the message
        await message.channel.send('General Kenobi')
    # Lets add a few more 
    if 'blind' in message.content.lower() and message.author.id != client.user.id:
        # This is another condition that would spam itself because the keyword 'blind' is present in the bot reply
        # This would cause the bot to spam-reply itself, in an undending loop.
        # to get around this, I had the bot grab its own user id (client id) from the client object and check it against the user that sent the message.
        # So in the case that the keyword is present in a message, but that message came from the bot itself. It will not reply.
        await message.channel.send('So love has blinded you?')

    if 'high' and 'ground' in message.content.lower() and message.author.id != client.user.id:
        await message.channel.send('I have the high ground Anakin')
    
    if 'try' in message.content.lower() and message.author.id != client.user.id:
        await message.channel.send('Do or do not, there is no try.')



# This line will run our client and should go at the bottom of our program
# It takes the bot token as a parameter
client.run(token)