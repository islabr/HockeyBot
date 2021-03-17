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