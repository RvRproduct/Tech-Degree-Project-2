"""
Python Web Development Techdegree
Project 2 - Basketball Stats Tool
Roberto Valentino Reynoso
8/7/2020
--------------------------------
"""

import constants
import copy
import re
import sys
import random

TEAMS = copy.deepcopy(constants.TEAMS)
PLAYERS = copy.deepcopy(constants.PLAYERS)


def menu():
    print("""Info: This program will set-up teams for the teams:
Panthers, Bandits, and Warriors. This program will choose the
players by random, and it will give you the option to view each
team list and it's stats, if you want to randomize the teams
again, just tell the program (NO that you would not like to view
another team) and go back to the main menu to restart the process
over again.\n""")
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


def balance_teams():
    cycle_amount = 0
    player_name = []
    player_select = []
    player_guardian = []
    player_guardian_select = []
    total_experienced = 0
    total_inexperienced = 0
    total_height = 0
    height_grab = 0
    player_grab = ""
    guardian_grab = ""
    team_panthers = ()
    guardians_panthers = ()
    height_panthers = 0
    experienced_panthers = 0
    inexperienced_panthers = 0
    team_bandits = ()
    guardians_bandits = ()
    height_bandits = 0
    experienced_bandits = 0
    inexperienced_bandits = 0
    team_warriors = []
    guardians_warriors = []
    height_warriors = 0
    experienced_warriors = 0
    inexperienced_warriors = 0

#unpacking the returns from clean_data()
    player_experience, player_height, player_guardian, player_name = clean_data()

#balancing out the teams, which is randomized        
    while True:
        player_roll_choice = random.randint(0, (len(player_name) - 1))
        
        if total_experienced != 3 and player_experience[player_roll_choice] == True:
            player_grab = player_name.pop(player_roll_choice)
            guardian_grab = player_guardian.pop(player_roll_choice)
            height_grab = player_height.pop(player_roll_choice)
            del player_experience[player_roll_choice]

            total_experienced += 1
            player_select.append(player_grab)
            player_guardian_select.extend(guardian_grab)
            total_height += height_grab
            cycle_amount += 1
            

        elif total_inexperienced != 3 and player_experience[player_roll_choice] == False:
            player_grab = player_name.pop(player_roll_choice)
            guardian_grab = player_guardian.pop(player_roll_choice)
            height_grab = player_height.pop(player_roll_choice)
            del player_experience[player_roll_choice]
            
            total_inexperienced += 1
            player_select.append(player_grab)
            player_guardian_select.extend(guardian_grab)
            total_height += height_grab
            cycle_amount += 1
            
        
        elif cycle_amount == 6 and len(team_panthers) == 0:
            team_panthers=tuple(player_select)
            guardians_panthers=tuple(player_guardian_select)
            player_select.clear()
            player_guardian_select.clear()
            height_panthers = total_height
            experienced_panthers = total_experienced
            inexperienced_panthers = total_inexperienced
            total_height = 0
            total_experienced = 0
            total_inexperienced = 0
            cycle_amount = 0
            
            

        elif cycle_amount == 6 and len(team_bandits) == 0:
            team_bandits=tuple(player_select)
            guardians_bandits=tuple(player_guardian_select)
            player_select.clear()
            player_guardian_select.clear()
            height_bandits = total_height
            experienced_bandits = total_experienced
            inexperienced_bandits = total_inexperienced
            total_height = 0
            total_experienced = 0
            total_inexperienced = 0
            cycle_amount = 0
            break

    for player in player_name:
        team_warriors.append(player)

    for guardian in player_guardian:
        guardians_warriors.extend(guardian)

    for height in player_height:
        height_warriors += height

    for experience in player_experience:
        if experience == True:
            experienced_warriors += 1
        elif experience == False:
            inexperienced_warriors += 1
            
    return (team_panthers, team_bandits, team_warriors, height_panthers, height_bandits, height_warriors, experienced_panthers, experienced_bandits, experienced_warriors, inexperienced_panthers, inexperienced_bandits, inexperienced_warriors, guardians_panthers, guardians_bandits, guardians_warriors)


def clean_data():
    player_experience = []
    player_height = []
    player_guardian = []
    player_name = []

    for player in PLAYERS:
        player_name.append(player["name"])

        if player["experience"] == "YES":
            player_experience.append(True)
        else:
            player_experience.append(False)

        player_height_process = player["height"]
        player_height.append(int(re.search(r"\d+", player_height_process).group()))

        player_guardian.append(player["guardians"].split("and"))

    return (player_experience, player_height, player_guardian, player_name)
        

def displaying_stats():
#unpacking the returns from balance_teams()
    (team_panthers, team_bandits, team_warriors, height_panthers, height_bandits, height_warriors, experienced_panthers, experienced_bandits, experienced_warriors, inexperienced_panthers, inexperienced_bandits, inexperienced_warriors, guardians_panthers, guardians_bandits, guardians_warriors) = balance_teams()
    choice = ""
    while True:
        print("""\nWould you like to select a team (1-2)?  
1) YES
2) NO\n""")
        choice = input("Enter an option (1-2) > ")
        if choice == "1":
            team_option = team_selection()
            if team_option == "Team: Panthers Stats":
                separator = ", "
                print(f"\n{team_option}")
                print("-" * 25)
                print(f"""Total players: {len(team_panthers)}
Total experienced: {experienced_panthers}
Total inexperienced: {inexperienced_panthers}
Average height: {height_panthers / len(team_panthers):.1f}\n""")
                print(f"Players on Team:\n  {separator.join(str(p) for p in team_panthers)}")
                print(f"Guardians:\n  {separator.join(str(g) for g in (guardians_panthers))}")

            elif team_option == "Team: Bandits Stats":
                separator = ", "
                print(f"\n{team_option}")
                print("-" * 25)
                print(f"""Total players: {len(team_bandits)}
Total experienced: {experienced_bandits}
Total inexperienced: {inexperienced_bandits}
Average height: {height_bandits / len(team_bandits):.1f}\n""")
                print(f"Players on Team:\n  {separator.join(str(p) for p in team_bandits)}")
                print(f"Guardians:\n  {separator.join(str(g) for g in (guardians_bandits))}")

            elif team_option == "Team: Warriors Stats":
                separator = ", "
                print(f"\n{team_option}")
                print("-" * 25)
                print(f"""Total players: {len(team_warriors)}
Total experienced: {experienced_warriors}
Total inexperienced: {inexperienced_warriors}
Average height: {height_warriors / len(team_bandits):.1f}\n""")
                print(f"Players on Team:\n  {separator.join(str(p) for p in team_warriors)}")
                print(f"Guardians:\n  {separator.join(str(g) for g in (guardians_warriors))}")
        elif choice == "2":
            break        


print("\nBASKETBALL TEAM STATS TOOL\n")
while True:
    menu_option = menu()
    if menu_option == "1":
        displaying_stats()
        
    input("\nPress Enter to continue...\n")
        


if __name__ == "__main__":
    menu()
    displaying_stats()
