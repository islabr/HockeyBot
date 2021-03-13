import requests
import argparse
import json
from extract_json import json_extract

def get_roster_team(team_num):
    url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num) + "/roster"

    response = requests.get(url)
    if response.status_code != 200:
        print("could not retrieve team")
        exit
    
    player_name = json_extract(response.json(), 'fullName')
    player_surname = []
    for player in player_name:
        first, last = player.split(' ')
        player_surname.append(last)
    player_id = json_extract(response.json(), 'id')
    player_info=dict(zip(player_surname,player_id))

    return player_info