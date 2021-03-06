# Star Wars Bot
##### Author: Adam Wahba

##### Date: 2021-03-04

##### For use by: Garth Webb Programming Club

This is a simple discord bot intended for use in servers to add inconvenient star wars memes and quotes.
This program will be updated over time. See version guide in the Source Code folder.
#### Purpose:
This program is also to be used as a learning example for anyone who wants to learn how to make their own discord bots.
This project will contain documentation regarding how to create a discord bot using discord's Python API. More detail below.

#### Why Python?

I chose Python for this example program because Python is more beginner friendly than other popular programming languages for discord bots such as JavaScript(Node.js), Java or C#.

#### Requirements

-Discord Module
-Python version 3.5 or later 
*Installing the discord module using pip*
pip is the Python package manager, used to install 3rd party modules/packages for Python.
We will need to install discord's python module that will let us use their API.
To do this, open a terminal, command prompt, or any other shell and use the following command
###### pip install discord


#### Discord Bots, clients and the discord API

##### Introduction

To create a discord bot(or any type of web-bot), you must first have an understanding of how apps and programs communicate to servers. In this case, how a program communicates to discord's servers.

##### Discord servers and clients

Anything that communicates to discord's servers is known as a "client". For example, the discord application on your phone and/or computer is a discord client. Clients communicate with servers using an API(Application-Program-Interface). In simple terms, an API is what allows a program like the discord app on your phone to send and request data to/from the discord server. When you send a message from the discord app, it will send the content of the message to the discord server via the discord API. This Client/Server communication is known as the back-end of a web application.

##### Why do I need to know what a client is?

You will need to know what a client is because your program, your discord bot is going to be a client on discord's servers. Having an understanding of how your bot is "talking" to discord is going to help you during your bot's development when you are going through Discord's public Python API.

##### The Discord API

The Discord API Documentation can be found with this link; https://discordpy.readthedocs.io/en/latest/api.html
To use the discord API you must have Python installed on your computer as well as the discord module.

#### Asynchronous Programming 

I will not go very in depth with Asynchronous Programming because it is its own topic and deserves its own example program. I will however, provide some explanations regarding what it is and why its used with discord bots.

##### Basic explanation

When a function is Asynchronous, that means that it will not block other processes within the program. So if 2 asynchronous functions are called one after the other within a program, the one called first will not block the 2nd function from running until its done. Instead, the program will rapidly switch between processing both functions. This means that it is possible for the 2nd function to finish before the 1st function although it was called after the 1st function. 
(Do not confuse this with threading, the program's processes are not running in parallel. They are running asynchronously in rapid alternation)

##### Async/Await Syntax, Why is it used in the bot?

An asynchronous function can be identified with the *async* syntax. When looking through the source code behind this bot, you may notice that every function is defined with this syntax as well as the *await* syntax for code within the function.
Discord bots need to be asynchronous programs because they send and receive data from discord's servers constantly. Asynchronous functions are meant to prevent the code from taking too long to execute one or more of its functions once they are called.