import constants
import copy
import re
import sys
import random

TEAMS = copy.deepcopy(constants.TEAMS)
PLAYERS = copy.deepcopy(constants.PLAYERS)


def menu():
    print("\n----MENU----")
    choices = ("Display Team Stats", "Quit",)
    selection = ""

    while selection.lower() != "2":
        print("\nHere are your choices:")
        for index, choice in enumerate(choices, 1):
            print(f"{index}) {choice}")

        selection = input("\nEnter an option (1-2) > ") 
        
        if selection == "1":
            return "1"

        elif selection.lower() in("2", "quit"):
            sys.exit()


def balance_teams():
    cycle_amount = 0
    player_name = []
    player_select = []
    player_guardian = []
    player_guardian_select = []
    total_experienced = 0
    total_inexperienced = 0
    total_height = 0
    player_grab = ""
    guardian_grab = ""

    player_experience, player_height = clean_data()
    num_players_team = int(len(PLAYERS) / len(TEAMS))
#using extend here for guardians, but it seems to delete info or gather incorrect data, if I append it,
#Gathers the correct data, but prints incorrectly
    for player in PLAYERS:
        player_name.append(player["name"])
        player_guardian.extend(player["guardians"].split("and"))

    while cycle_amount < num_players_team:
        player_roll_choice = random.randint(0, (len(player_name) - 1))
       
        if total_experienced < 3 and player_experience[player_roll_choice] == True:
            player_grab = player_name.pop(player_roll_choice)
            guardian_grab = player_guardian.pop(player_roll_choice)

            total_experienced += 1
            player_select.append(player_grab)
            player_guardian_select.append(guardian_grab)
            total_height += player_height[player_roll_choice]
            cycle_amount += 1

        elif total_inexperienced < 3 and player_experience[player_roll_choice] == False:
            player_grab = player_name.pop(player_roll_choice)
            guardian_grab = player_guardian.pop(player_roll_choice)
            
            total_inexperienced += 1
            player_select.append(player_grab)
            player_guardian_select.append(guardian_grab)
            total_height += player_height[player_roll_choice]
            cycle_amount += 1

    return (player_select, num_players_team, player_guardian_select, total_experienced, total_inexperienced, total_height)


def team_selection():
    choice = ""
    print()
    while choice.lower() != "quit":
        for index, team in enumerate(TEAMS, 1):
            print(f"{index}) {team}")
        choice = input("\nEnter an option (1-3) > ")

        if choice == "1":
            return "Team: Panthers Stats"

        elif choice == "2":
            return "Team: Bandits Stats"

        elif choice == "3":
            return "Team: Warriors Stats"



def clean_data():
    player_experience = []
    player_height = []

    for player in PLAYERS: 
        if player["experience"] == "YES":
            player_experience.append(True)
        else:
            player_experience.append(False)

        player_height_process = player["height"]
        player_height.append(int(re.search(r"\d+", player_height_process).group()))

    return (player_experience, player_height)
        

def displaying_stats():
    player_team_names, total_num_players, player_guardian_names, total_experienced, total_inexperienced, total_height = balance_teams()
    separator = ", "
    print(f"\n{team_option}")
    print("-" * 25)
    print(f"""Total players: {total_num_players}
Total experienced: {total_experienced}
Total inexperienced: {total_inexperienced}
Average height: {total_height / total_num_players:.1f}\n""")
    print(f"Players on Team:\n  {separator.join(str(p) for p in player_team_names)}")
    print(f"Guardians:\n  {separator.join(str(g) for g in (player_guardian_names))}")


print("BASKETBALL TEAM STATS TOOL\n")
while True:
    menu_option = menu()

    if menu_option == "1":
        team_option = team_selection()

    if team_option in("Team: Panthers Stats", "Team: Bandits Stats", "Team: Warriors Stats"):
        displaying_stats()

    input("Press Enter to continue...")


if __name__ == "__main__":
    menu()
    team_selection()
    displaying_stats()
