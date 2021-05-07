# bot.py
import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from get_roster import get_team_roster
from get_player import get_player_stats
from get_team import get_team_id, get_team_stats

client = discord.Client()
load_dotenv()
TOKEN = ""

def get_t_stats(team):
  id = get_team_id(team)

  stats = get_team_stats(id)
  return(stats)


def get_p_stats(team, player):
  id = get_team_id(team)

  roster = get_team_roster(id)

  roster_json = json.dumps(roster, indent = 4)   
  resp = json.loads(roster_json)

  stats = get_player_stats(id, player)
  return(stats)

  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('stat'):
    words = msg.split(" ")
  #  if len(words) == 2:
 #     team = words[1]
   #   stats = get_t_stats(team)
    if len(words) == 3:
      team = words[1]
      player = words[2]
      stats = get_p_stats(team, player)
    elif len(words) == 4:
      player = words[2] + " " + words[3]
      team = words[1]
      stats = get_p_stats(team, player)
   # elif len(words) == 2:
   #   team = words
   #   stats = get_t_stats(words[1])
    await message.channel.send(stats)

client.run(TOKEN)