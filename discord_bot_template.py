import discord
import asyncio

import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()
commands = {}

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
    
    if keyword in commands.keys:
        await commands[keyword](commandObj)
    else:
        await client.send_message(commandObj.channel, "Unknown command")
        
async def test_command(commandObj):
    await client.send_message(commandObj.channel, "message recived")

commands["test"] = test_command
client.run('token')