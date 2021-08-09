import requests
from get_roster import get_team_roster
from extract_json import json_extract

def format_skater_stats(json_data, name):
  #TODO: add more stats
  goals  = json_extract(json_data, 'goals')
  shots = json_extract(json_data, 'shots')
  games = json_extract(json_data, 'games')

  stats = ("--- **{0}** ---\nGames Played : `{1}`\nShots: `{2}`\nGoals: `{3}`"
           .format(name[0], games[0], shots[0], goals[0]))
  return stats


def format_goalie_stats(json_data, name):
  #TODO: add more stats
  games = json_extract(json_data, 'games')
  saves  = json_extract(json_data, 'saves')
  shutouts = json_extract(json_data, 'shutouts')
  shots_against = json_extract(json_data, 'shotsAgainst')
  goals_against = json_extract(json_data, 'goalsAgainst')
  
  stats = ("--- **{0}** ---\nGames Played : `{1}`\nSaves: `{2}`\nShots Against: "\
           "`{3}`\nGoals Against: `{4}`\nShutouts: `{5}`".format(name[0], games[0], saves[0], 
           shots_against[0], goals_against[0], shutouts[0]))
  return stats


def get_player_details(player_id):
  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id)
  response = requests.get(url)
  if response.status_code != 200:
    return("could not retrieve player")
  name = json_extract(response.json(), 'fullName'),
  position = json_extract(response.json(), 'code')
  return name, position


def get_player_stats(team, player_name):
  team_roster = get_team_roster(team)
  player_id = team_roster[player_name]

  url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id) + "/stats?stats=statsSingleSeason&season=20202021"
  
  response = requests.get(url)
  if response.status_code != 200:
    return("could not retrieve player")

  player_name, player_position = get_player_details(player_id)

  if player_position[0] == "G":
    stats = format_goalie_stats(response.json(), player_name[0])
  else:
    stats = format_skater_stats(response.json(), player_name[0])
  return stats
