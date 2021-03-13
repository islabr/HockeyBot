# bot.py
import discord
import os
import requests
import json
import random
from dotenv import load_dotenv

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(os.getenv('DISCORD_TOKEN'))

def get_quote():
  response = requests.get("https://statsapi.web.nhl.com/api/v1/")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$team'):
    for word in msg
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(TOKEN)