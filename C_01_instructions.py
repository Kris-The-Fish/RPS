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


# Main routine
print()
print("💎📃✂️Rock / Paper / Scissors Game !✂️📃💎")
print()
# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")


