import requests
import json

def format_team_statistics(data):
  #TODO: add stats
  return "Team statistics unavaliable during offseason."


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
  id = team[team_name]
  return id


def get_team_info(team_num, type):
  url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num)
  print(url)
  response = requests.get(url)
  if response.status_code != 200:
      return("could not retrieve team")

  if type == "D":
    data = format_team_details(response.json())
  elif type == "S":
     data = format_team_statistics(response.json())
  return data