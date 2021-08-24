import requests
from get_roster import get_team_roster, get_team_abbreviation
import matplotlib.pyplot as plt
from matplotlib import cbook
import re


#TODO: Clean up code
def get_player_history(team, player_name):
  url_list, goals, season, assists, shots, points = ([] for _ in range(6))

  team_roster = get_team_roster(team)
  abbreviation = get_team_abbreviation(team)
  player_id = team_roster[player_name]
  base_url = "https://statsapi.web.nhl.com/api/v1/people/" + str(player_id) + "/stats?stats=statsSingleSeason&season="
  
  season_2021 = base_url + "20202021"
  season_1920 = base_url + "20192020"
  season_1819 = base_url + "20182019"
  season_1718 = base_url + "20172018"
  season_1617 = base_url + "20162017"
  season_1516 = base_url + "20152016"

  url_list.extend((season_1516,season_1617,season_1718,season_1819,season_1920,season_2021))

  for url in url_list:
    response = requests.get(url)
    if response.status_code != 200:
      return("could not retrieve player")
    try:
      data = response.json()
      details = data['stats'][0]['splits'][0]
      year_goals = details['stat']['goals']
      current_season = details['season']
      year_assists = details['stat']['assists']
      year_shots = details['stat']['shots']
      year_points = details['stat']['points']
      goals.append(year_goals)
      season.append(current_season)
      assists.append(year_assists)
      shots.append(year_shots)
      points.append(year_points)
    except IndexError:
      print("skip")
  season = split_seasons(season)
  generate_graph(abbreviation, season, goals, assists, shots, points, player_name)
  return

def split_seasons(seasons):
    reg = "20(\d\d)20(\d\d)"
    for i in range(len(seasons)):
        x = re.search(reg, seasons[i])
        seasons[i] = x.group(1) + "/" + x.group(2)
    return seasons

def generate_graph(abbreviation, season, goals, assists, shots, points, player):
  
  fig, axs = plt.subplots(2, 2)
  plt.title(player)

  #goals graph
  axs[0, 0].plot(season,goals, color='blue')
  axs[0, 0].set_title("Goals")
  axs[0, 0].set_ylim(bottom=(min(goals)-5), top=(max(goals)+5))

  #points graph
  axs[1, 0].plot(season, points, color='red')
  axs[1, 0].set_title("Points")
  axs[1, 0].set_ylim(bottom=(min(points)-5), top=(max(points)+5))

  #assists graph
  axs[0, 1].plot(season, assists, color='green')
  axs[0, 1].set_title("Assists")
  axs[0, 1].set_ylim(bottom=(min(assists)-5),top=(max(assists)+5))

  #shots graph
  axs[1, 1].plot(season, shots, color='orange')
  axs[1, 1].set_title("Shots")
  axs[1, 1].set_ylim(bottom=(min(shots)-20), top=(max(shots)+10))
  
  img_path = "./images/" + abbreviation + ".png"
  image = plt.imread(img_path)
 # plt.imshow(image)

  newax = fig.add_axes([0.8, 0.8, 0.2, 0.2], anchor='NE', zorder=-1)
  newax.imshow(image)
  newax.axis('off')

  fig.tight_layout(pad=0)
  fig.savefig('player_history.png',transparent=True)
  return