rock = '''Rock!\n
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper!\n
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors!\n
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_throws = [rock, paper, scissors]

messages = {
    "welcome": "Welcome to Rock, Paper, Scissors\n",
    "player_choice": 'What do you choose? "0" for rock, "1" for paper and "2" for scissors -->',
    "continue?": "Want to continue? (Y)es/(N)o? -->",
    "error_choice": '\nYou should choose a number between "0", "1" and "2" -->',
    "win": "Congratulations, you win! :)\n",
    "lose": "Oh no, you lost :(\n",
    "draw": "It's a draw!\n",
    "thanks": "\nThank you for playing!\n",
    "continue_error": "\nNot a valid answer. Quitting game!\n"
}
