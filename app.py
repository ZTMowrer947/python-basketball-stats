"""Basketball stats application"""
# import PLAYERS, TEAMS from constants

# function clean_data
# with parameter players
    # define cleaned_players, set to empty list

    # for each player in players
        # define cleaned_player, set to empty dictionary
        # for each key/value pair in player
            # define cleaned_value, set to value
            # if key is height
                # set cleaned_value to result of coercing value to integer
            # else if key is experience
                # set cleaned_value to result of if value is equal to YES
            # end if

            # add key of key to cleaned_player, setting value to cleaned_value
        # end for

        # append cleaned_player to list cleaned_players
    # end for

    # return cleaned_players
# end function

# function balance_teams
# with parameter cleaned_players
# and parameter teams
    # define players_per_team, set to quotient of length of cleaned_players list and length of teams list
    # define teams_with_players, set to empty dictionary

    # for each index, team in enumeration of teams
        # define start, set to product of index and players_per_team
        # define end, set to sum of start and players_per_team

        # define players_on_team, set to slice of cleaned_players from start to end

        # add key of team to teams_with_players, setting value to players_on_team
    # end for

    # return teams_with_players
# end function

if __name__ == '__main__':
    pass
