# bot.py
import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from get_player_info import get_roster_team
from get_player import get_player_stats
from get_team import get_team_id


client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(os.getenv('DISCORD_TOKEN'))


def get_stats(team, player):

  id = get_team_id(team)

  roster = get_roster_team(id)

  roster_json = json.dumps(roster, indent = 4)   
  resp = json.loads(roster_json)

  stats = get_player_stats(id, player)
  print(stats)
  return(stats)

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
        player = words[2] + " " + words[3]
        team = words[1]
    
    stats = get_stats(team, player)
    await message.channel.send(stats)

client.run(TOKEN)