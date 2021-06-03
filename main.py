import gamelogic
import assets

print(assets.messages["welcome"])

game_loop = True

while game_loop is True:

    player_choice = gamelogic.get_player_input(
        assets.messages["player_choice"])

    player_choice = gamelogic.check_if_valid_player_input(player_choice)

    computer_choice = gamelogic.computer_choice()

    gamelogic.print_choices(player_choice, computer_choice)

    gamelogic.throw_comparison(player_choice, computer_choice)

    player_choice = gamelogic.get_player_input(assets.messages["continue?"])

    if gamelogic.want_to_continue(player_choice) is False:
        game_loop = False