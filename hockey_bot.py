# bot.py
import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from checker import get_stats

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(os.getenv('DISCORD_TOKEN'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('stat'):
    words = msg.split(" ")
    if len(words) == 3:
        team = words[1]
        player = words[2]
    elif len(words) == 4:
        team = words[1] + " " + words[2]
        player = words[3]
    
    stats = get_stats(team, player)
    await message.channel.send(stats)

client.run(TOKEN)