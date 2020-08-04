import constants
import copy

TEAMS = copy.deepcopy(constants.teams())
PLAYERS = copy.deepcopy(constants.players())


def menu():
    choices = ("Display Team Stats", "Quit",)
    selection = ""
    while selection.lower() != "2":
        print("\nHere are your choices:")
        for index, choice in enumerate(choices, 1):
            print(f"{index}) {choice}")
        selection = input("\nEnter an option > ") 


def balance_teams():
    num_players_team = len(PLAYERS) / len(TEAMS)
    return num_players_team


def show_team_selection():
    for index, team in enumerate(TEAMS, 1):
        print(f"{index}) {team}")


def clean_data():
    players_convert = {}
    for player in PLAYERS:
        players_convert.update(player)
        
    print(players_convert)


clean_data()
show_team_selection()

print("BASKETBALL TEAM STATS TOOL\n")

menu()
        