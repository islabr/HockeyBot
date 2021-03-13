import json
import argparse
from get_roster import get_roster_team
from get_player import get_player_stats
from get_team import get_team_id

def main(team, player):

  id = get_team_id(team)

  roster = get_roster_team(id)

  roster_json = json.dumps(roster, indent = 4)   
  resp = json.loads(roster_json)

  stats = get_player_stats(id, player)
  print(stats)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='flags')
    parser.add_argument("-t", "--team")
    parser.add_argument("-p", "--player")
    args = parser.parse_args()
    main(args.team, args.player)