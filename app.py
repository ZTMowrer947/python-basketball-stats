"""Basketball stats application"""
from constants import PLAYERS, TEAMS


def clean_data(players):
    cleaned_players = []

    for player in players:
        cleaned_player = {}

        for key, value in player.items():
            cleaned_value = value

            if key == "height":
                cleaned_value = int(value[0:2])
            elif key == "experience":
                cleaned_value = value == "YES"

            cleaned_player[key] = cleaned_value

        cleaned_players.append(cleaned_player)

    return cleaned_players


def balance_teams(cleaned_players, teams):
    players_per_team = len(cleaned_players) // len(teams)
    teams_with_players = {}

    for index, team in enumerate(teams):
        start = index * players_per_team
        end = start + players_per_team

        players_on_team = cleaned_players[start:end]

        teams_with_players[team] = players_on_team

    return teams_with_players


if __name__ == '__main__':
    cleaned_players = clean_data(PLAYERS)
    teams_with_players = balance_teams(cleaned_players, TEAMS)

    for team, players in teams_with_players.items():
        print(team)
        for player in players:
            print(player)
