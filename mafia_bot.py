import discord
import asyncio
import random

import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()
commands = {}

tempChannels = []
started = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        await handle_command(message)
        
        
async def handle_command(commandObj):
    keyword = commandObj.content[1:].split()[0]
    
    if keyword in commands.keys():
        await commands[keyword](commandObj)
    else:
        await client.send_message(commandObj.channel, "Unknown command")
        
async def start_game(commandObj):
    global started
    global tempChannles
    
    if not started:
        started = True
        await client.send_message(commandObj.channel, "Starting game. Please wait.")
        server = commandObj.server
        client.create_channel(server, 'Mafia', type=discord.ChannelType.voice)
        
        users = []
        mafia = []
        villagers = []
        
        for usr in server.members:
            if usr.top_role.name != "MafiaBot":
                users.append(usr)        
                
        for i in range(3):
            mafia.append(random.choice(users))
        
        for usr in users:
            if usr not in mafia:
                villagers.append(usr)
        
        client.create_channel(server, 'Mafia', type=discord.ChannelType.voice)
                
        #for usr 
        
    else:
        await client.send_message(commandObj.channel, "Game already in progress.")
    
    users = []
    #for usr in commandObj.channel

commands["startgame"] = start_game
client.run('MzgyODk3MTUzNjExMTM3MDI3.DQNoqg.6hfOFCwMAKSty3QApxSygGmEckE')