"""Basketball stats application"""
from constants import PLAYERS, TEAMS


def clean_data(players):
    """Sanitize the list of player data."""
    cleaned_players = []

    for player in players:
        cleaned_player = {}

        for key, value in player.items():
            cleaned_value = value

            if key == "height":
                cleaned_value = int(value[0:2])
            elif key == "experience":
                cleaned_value = value == "YES"
            elif key == "guardians":
                cleaned_value = value.split(" and ")

            cleaned_player[key] = cleaned_value

        cleaned_players.append(cleaned_player)

    return cleaned_players


def balance_teams(players, teams):
    """
    Split the given list of players into teams such that
    each team has an equal number of players.
    """
    players_per_team = len(players) // len(teams)
    teams_with_players = {}

    # Split players based on whether they are experienced
    experienced_players = [player for player in players if player['experience'] is True]
    inexperienced_players = [player for player in players if player not in experienced_players]

    for index, team in enumerate(teams):
        start = index * players_per_team // 2
        end = start + players_per_team // 2

        players_on_team = experienced_players[start:end]
        players_on_team.extend(inexperienced_players[start:end])

        teams_with_players[team] = players_on_team

    return teams_with_players


def select_item_from_menu(options):
    """
    Displays a menu for the provided list of options, then repeated prompts the user
    for an option until a valid one is selected, then returns the selected option.
    """

    # Setup menu
    valid_index_range = range(0, len(options))
    selected_index = -1
    while selected_index not in valid_index_range:
        try:
            # Print menu
            for index, team in enumerate(options):
                team_num = index + 1

                print(f"{team_num}) {team}")

            # Prompt user for selection
            selected_index = int(input("\nPlease select an option: ")) - 1
        except ValueError:
            print(f"Invalid option!\n")
        else:
            if selected_index not in valid_index_range:
                print("Option not in range!\n")

    selected_item = options[selected_index]
    return selected_item


if __name__ == '__main__':
    # Setup teams
    cleaned_players = clean_data(PLAYERS)
    teams_with_players = balance_teams(cleaned_players, TEAMS)

    # Print introductory menu
    print("Basketball Team Statistics Tool")
    intro_menu_options = ["Display Team Statistics", "Exit"]
    selected_option = select_item_from_menu(intro_menu_options)

    print()

    # User chose to display stats for a team
    if selected_option == intro_menu_options[0]:
        # Prompt user for team to select
        selected_team = select_item_from_menu(TEAMS)
        team_players = teams_with_players[selected_team]

        # Print team data
        print(f"\n{selected_team} Team Statistics")
        print("------------------------------------")
        print(f"Total players: {len(team_players)}\n")
        print("Players on the team:")

        player_names = [player['name'] for player in team_players]
        joined_names = ", ".join(player_names)
        print(f"\t{joined_names}")
    # User chose to exit
    else:
        print("Bye")


