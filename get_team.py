import requests
import json

def format_team_statistics(data):
  #TODO: add stats
  details = data['stats'][0]['splits'][0]
  team = details['team']['name']
  gp = details['stat']['gamesPlayed']
  w = details['stat']['wins']
  l = details['stat']['losses']
  pts = details['stat']['pts']
  if int(l) > 0 and int(w) > 0:
    percent = (int(l)/int(w))*100
  else:
    percent = 0
  details = ("--- **{0}** ---\nGames Played : `{1}`\nWins: `{2}`\nLosses: `{3}`\
             \nPoints: `{4}`\nWin Percentage:`{5}%`".format(team, gp, w, l, pts, round(percent)))
  return details


def format_team_details(data):
  team = data['teams'][0]['name']
  conference = data['teams'][0]['conference']['name']
  division = data['teams'][0]['division']['name']
  fyop = data['teams'][0]['firstYearOfPlay']
  site = data['teams'][0]['officialSiteUrl']
  details = ("--- **{0}** ---\nConference : *{1}*\nDivision: *{2}*\nFirst Year Of Play: *{3}*\
           \n\n**Visit**: {4}".format(team, conference, division, fyop, site))
  return details
  

def get_team_id(team_name):
  # read file
  with open('teams.json', 'r') as myfile:
      data=myfile.read()

  # parse file
  team = json.loads(data)
  try:
    id = team[team_name]
  except:
    return 'invalid team "%s"' % str(team_name)
  return id


def get_team_info(team_num, type):
  if type == "D":
    url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num)
    response = requests.get(url)
    if response.status_code != 200:
      return("could not retrieve team")
    data = format_team_details(response.json())
  elif type == "S":
    url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num) + "/stats?stats=statsSingleSeason&season=20212022"
    response = requests.get(url)
    if response.status_code != 200:
      return("could not retrieve team")
    data = format_team_statistics(response.json())
  return data