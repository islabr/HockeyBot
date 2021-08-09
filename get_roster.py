import requests
from extract_json import json_extract

def get_team_roster(team_num):
    url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(team_num) + "/roster"

    response = requests.get(url)
    if response.status_code != 200:
        return("could not retrieve team")
    
    player_name = json_extract(response.json(), 'fullName')
    player_surname = []
   
    for player in player_name:
        spaces=0
        for character in player:
            if(character.isspace()):
                spaces=spaces+1
        if spaces == 1:
            first, last = player.split(' ')
        elif spaces == 2:
            first, mid, last = player.split(' ')
            last = mid + " " + last
        player_surname.append(last)
    player_id = json_extract(response.json(), 'id')
    player_info=dict(zip(player_surname,player_id))

    return player_info