import constants
import copy


players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)


def clean_data():
    for player in players_copy:
        player_height = player['height'].split(" ")
        player_height_inches = int(player_height[0])
        player['height'] = player_height_inches

    for player in players_copy:
        player_experience = player['experience'] 
        if player_experience == "YES":
            player['experience'] = True
        elif player_experience == "NO":
            player['experience'] = False

def balance_teams():
    #  num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    #  print(num_players_team)
    Panthers = []
    Bandits = []
    Warriors = []
    teams = [Panthers, Bandits, Warriors]
    num_players = len(teams)
    for num in range(len(players_copy)):
        teams[num % num_players].append(players_copy[num])
    return (Panthers, Bandits, Warriors)


def menu():
    while True:
        print("BASKETBALL TEAM STATS TOOL\n")
        print("-" * 4, "MENU", "-" * 4)
        print("\nWhat would you like to do?\n")
        print("\nA) Display Team Stats")
        print("B) Quit\n")

        try:
            option = input("Please, enter A or B. --> ")

        except TypeError:
            print("Oops, you need to enter A or B.")
            continue

        if option.upper() == "A":
            print("\nWhich team's stats do you want to check out?")
            print("A) Panthers")
            print("B) Bandits")
            print("C) Warriors")

            selected_team = input("\nPlease, enter A, B, or C. --> ")
            if selected_team.upper() == "A":
                panthers_list = balance_teams()[0]
                players = len(panthers_list)
                print("\nTeam: Panthers")
                print("-" * 14)
                print("Total players: {}\n".format(players))
                panthers_players_names = []

                for player in panthers_list:
                    names = player['name']
                    panthers_players_names.append(str(names))
                print(", ".join(panthers_players_names))

            elif selected_team.upper() == "B":
                bandits_list = balance_teams()[1]
                players = len(bandits_list)
                print("\nTeam: Bandits")
                print("-" * 14)
                print("Total players: {}\n".format(players))
                bandits_players_names = []

                for player in bandits_list:
                    names = player['name']
                    bandits_players_names.append(str(names))
                print(", ".join(bandits_players_names))

            elif selected_team.upper() == "C":
                warriors_list = balance_teams()[2]
                players = len(warriors_list)
                print("\nTeam: Warriors")
                print("-" * 14)
                print("Total players: {}\n".format(players))
                warriors_players_names = []

                for player in warriors_list:
                    names = player['name']
                    warriors_players_names.append(str(names))
                print(", ".join(warriors_players_names))

        elif option.upper() == "B":
            break


if __name__ == "__main__":
    clean_data()
    balance_teams()
    menu()
