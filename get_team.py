import requests
import argparse
import json
from extract_json import json_extract

def get_team_id(team_name):
  # read file
  with open('teams.json', 'r') as myfile:
      data=myfile.read()

  # parse file
  obj = json.loads(data)
  id = obj[team_name]
  return id

def get_team_stats(team_num):
  url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num)

  response = requests.get(url)
  if response.status_code != 200:
      print("could not retrieve team")
      exit
    
  return 