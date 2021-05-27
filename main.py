import random

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

rock_paper_scissors_list = [rock, paper, scissors]

game_on = True

print("Welcome to Rock, Paper, Scissors\n")

while game_on is True:

    user_choice = int(input(
        '\nWhat do you choose? "0" for rock, "1" for paper and "2" for scissors\n\n'))

    if user_choice >= 3:
        print("\nYou should choose a number between 0, 1 and 2\n")
        continue_playing = input('Want to continue? "Y" or "N"?\n\n').lower()
        if continue_playing == "y":
            user_choice = int(input(
                'What do you choose? "0" for rock, "1" for paper and "2" for scissors\n\n'))
        else:
            break

    print(f"\nYou choose: {rock_paper_scissors_list[user_choice]}\n")

    computer_choice = random.randint(0, 2)
    print(
        f"\nThe computer chooses: {rock_paper_scissors_list[computer_choice]}\n")

    if user_choice == computer_choice:
        print("It's a draw!\n")
    elif ((user_choice == 0 and computer_choice == 1)
          or (user_choice == 1 and computer_choice == 2)
          or (user_choice == 2 and computer_choice == 0)):
        print("You lose :(\n")
    elif ((user_choice == 0 and computer_choice == 2)
          or (user_choice == 2 and computer_choice == 1)
          or (user_choice == 1 and computer_choice == 0)):
        print("You win! :)\n")

    continue_playing = input("Want to continue? Y or N?\n\n").lower()

    if continue_playing == "y":
        continue
    else:
        game_on = False
