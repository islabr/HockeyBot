# bot.py
import discord
from dotenv import load_dotenv
from tabulate import tabulate
from get_player import get_player_stats
from get_history import get_player_history
from get_team import get_team_id, get_team_info

client = discord.Client()
load_dotenv()
TOKEN = ""

def get_team(team, type):
  id = get_team_id(team)
  if "invalid team" not in str(id):
    info = get_team_info(id, type)
    return info
  return id


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

  msg = message.content.lower()

  #check for a help request
  if msg.startswith('hb help'):
      help = "**HOCKEY BOT HELP**\n\n To view the details of a team type: ```yaml\nhb detail <team name>\n```\
              \nTo view the current season statistics of a player, type ```yaml\nhb stat <team> <player surname>\n```\
              \nTo view the current season statistics of a team, type ```yaml\nhb stat <team>\n```\
              \nTo view the history of a player, type ```yaml\nhb history <team> <player surname>\n```"
      await message.channel.send(help)
      


  #check for a detail request
  if msg.startswith('hb detail'):
    words = msg.split(" ")
    if len(words) == 3:
      team = words[2]
      stats = get_team(team, "D")
      await message.channel.send(stats)
    else:
      await message.channel.send("**Invalid team entered**")

  #check for a history request
  if msg.startswith('hb history'):
    words = msg.split(" ")
    if len(words) == 4:
      team = words[2]
      player = words[3]
      stats = get_history(team, player.capitalize())
    elif len(words) == 5:
      player = words[3] + " " + words[4]
      team = words[2]
      stats = get_history(team, player.capitalize())
    if "Could not find" in str(stats):
      await message.channel.send(stats)
    else:
      await message.channel.send(file=discord.File('player_history.png'))
      

  #check for a statistics request
  if msg.startswith('hb stat'):
    words = msg.split(" ")
    if len(words) == 3:
      team = words[2]
      stats = get_team(team, "S")

    if len(words) == 4:
      team = words[2]
      player = words[3]
      stats = get_player(team, player.capitalize())

    elif len(words) == 5:
      player = words[3] + " " + words[4]
      team = words[2]
      stats = get_player(team, player.capitalize())
    await message.channel.send(stats)

client.run(TOKEN)