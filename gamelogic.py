import random
import assets


def get_player_input(text):
    print(text, end=' ')
    player_choice = input().lower()
    return player_choice


def check_if_valid_player_input(player_choice):
    while player_choice.isnumeric() is False:
        player_choice = get_player_input(assets.messages["error_choice"])

    player_choice = int(player_choice)

    while player_choice >= 3:
        player_choice = get_player_input(assets.messages["error_choice"])
        player_choice = check_if_valid_player_input(player_choice)

    return player_choice


def want_to_continue(player_choice):
    if player_choice == "n":
        print(assets.messages["thanks"])
        return False
    elif player_choice == "y":
        print("")
        return True
    else:
        print(assets.messages["continue_error"])
        return False


def computer_choice():
    computer_choice = random.randint(0, 2)
    return computer_choice


def print_choices(player_choice, computer_choice):
    print("")
    print(f"You choose: {assets.game_throws[player_choice]}")
    print(f"The computer chooses: {assets.game_throws[computer_choice]}")


def throw_comparison(player_choice, computer_choice):
    if player_choice == computer_choice:
        print(assets.messages["draw"])
    elif ((player_choice == 0 and computer_choice == 1)
            or (player_choice == 1 and computer_choice == 2)
            or (player_choice == 2 and computer_choice == 0)):
        print(assets.messages["lose"])
    elif ((player_choice == 0 and computer_choice == 2)
            or (player_choice == 2 and computer_choice == 1)
            or (player_choice == 1 and computer_choice == 0)):
        print(assets.messages["win"])
