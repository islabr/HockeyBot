import json
import requests
from get_player_info import get_team_roster
from extract_json import json_extract

def format_skater_stats_string(json_data, name):
  goals  = json_extract(json_data, 'goals')
  shots = json_extract(json_data, 'shots')
  games = json_extract(json_data, 'games')
  stats = ("---{0}---\nGames Played : {1}\nShots: {2}\nGoals: {3}".format(name[0], games[0], shots[0], goals[0]))
  return stats

def format_goalie_stats_string(json_data, name):
  games = json_extract(json_data, 'games')
  saves  = json_extract(json_data, 'saves')
  shutouts = json_extract(json_data, 'shutouts')
  shots_against = json_extract(json_data, 'shotsAgainst')
  goals_against = json_extract(json_data, 'goalsAgainst')
  
  stats = ("---{0}---\nGames Played : {1}\nShots Against: {2}\nGoals Against: {3}\nShutouts: {4}".format(name[0], games[0], shots_against[0], goals_against[0], shutouts[0]))
  return stats

def get_player_name(player_id):
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id)
  response = requests.get(url)
  name = json_extract(response.json(), 'fullName')
  return name

def get_player_position(player_id):
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id)
  response = requests.get(url)
  name = json_extract(response.json(), 'code')
  return name

def get_player_stats(team, player_name):
  team = get_team_roster(team)
  roster_json = json.dumps(team, indent = 4)   
  players = json.loads(roster_json)
  player_id = players[player_name]
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id) + "/stats?stats=statsSingleSeason&season=20202021"
  response = requests.get(url)
  if response.status_code != 200:
    print("could not retrieve player")
    exit
  player_name = get_player_name(player_id)
  player_position = get_player_position(player_id)
  if player_position[0] == "G":
    stats = format_goalie_stats_string(response.json(), player_name)
  else:
    stats = format_skater_stats_string(response.json(), player_name)
  return stats
