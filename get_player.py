import json
import requests
from get_player_info import get_roster_team
from extract_json import json_extract

team = 10


def format_stats_string(json_data, name):
  goals  = json_extract(json_data, 'goals')
  shots = json_extract(json_data, 'shots')
  games = json_extract(json_data, 'games')
  stats = ("---{0}---\nGames Played : {1}\nShots: {2}\nGoals: {3}".format(name[0], games[0], shots[0], goals[0]))
  return stats

def get_player_name(player_id):
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id)
  response = requests.get(url)
  name = json_extract(response.json(), 'fullName')
  return name

def get_player_stats(team, player_name):
  team = get_roster_team(team)
  roster_json = json.dumps(team, indent = 4)   
  players = json.loads(roster_json)
  player_id = players[player_name]
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id) + "/stats?stats=statsSingleSeason&season=20202021"
  response = requests.get(url)
  if response.status_code != 200:
    print("could not retrieve player")
    exit
  player_name = get_player_name(player_id)
  stats = format_stats_string(response.json(), player_name)
  return stats
