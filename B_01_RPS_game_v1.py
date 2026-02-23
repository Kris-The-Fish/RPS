# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response in a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    """prints instructions"""

    print("""
*** Instructions ****

 To begin, choose the number of rounds (or press <enter> for
  play infinite mode).

 Then play against the computer. You need to choose R (rock),
  P (paper), or S (scissors).

 The rules are as follows:
 - Paper beats Rock
 - Rock beats Scissors
 - Scissors beats Paper

 Press <xxx> to end the game at anytime>

 Good Luck !!!
    """)

def int_check(question):

    while True:
        error = "please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
              return response

        except ValueError:
            print(error)


# Main Routine Starts here

# Inialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print("💎📃✂️Rock / Paper / Scissors Game !✂️📃💎")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()


# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:


    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n 📀📀📀 Round {rounds_played + 1} (Infinite Mode) 📀📀📀"
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    user_choice = string_checker("Choose: ", rps_list)
    print("You chose", user_choice)

    if user_choice == "xxx":
        break

    rounds_played += 1

     # if users are infinite mode, increase number of rounds !
    if mode == "infinite":
        num_rounds += 1


# Game loop ends here


# Game History / Statistics area