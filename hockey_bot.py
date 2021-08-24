# bot.py
import discord
from dotenv import load_dotenv
from get_player import get_player_stats
from get_history import get_player_history
from get_team import get_team_id, get_team_info

client = discord.Client()
load_dotenv()
TOKEN = ""

def get_team(team, type):
  id = get_team_id(team)
  info = get_team_info(id, type)
  return(info)


def get_player(team, player):
  id = get_team_id(team)
  stats = get_player_stats(id, player)
  return(stats)

def get_history(team, player):
  id = get_team_id(team)
  stats = get_player_history(id, player)
  return(stats)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #check for a detail request
  if msg.startswith('detail'):
    words = msg.split(" ")
    if len(words) == 2:
      team = words[1]
      stats = get_team(team, "D")
      await message.channel.send(stats)
    else:
      await message.channel.send("*Invalid team entered*")

  #check for a history request
  if msg.startswith('history'):
    words = msg.split(" ")
    if len(words) == 3:
      team = words[1]
      player = words[2]
      stats = get_history(team, player)

    elif len(words) == 4:
      player = words[2] + " " + words[3]
      team = words[1]
      stats = get_history(team, player)
    await message.channel.send(file=discord.File('player_history.png'))

  #check for a statistics request
  if msg.startswith('stat'):
    words = msg.split(" ")
    if len(words) == 2:
      team = words[1]
      stats = get_team(team, "S")

    if len(words) == 3:
      team = words[1]
      player = words[2]
      stats = get_player(team, player)

    elif len(words) == 4:
      player = words[2] + " " + words[3]
      team = words[1]
      stats = get_player(team, player)
    await message.channel.send(stats)

client.run(TOKEN)