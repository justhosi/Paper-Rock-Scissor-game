import random

print('Welcome to Paper-Rock-Scissor game By JustHosi.\nLet\'s play...\n' )

def machine_choice():
    computer_choices = ['p', 's', 'r']
    computer_choice = random.choice(computer_choices)  # computer picks either of computer choices by random
    return computer_choice


def resault(user_choice):   #compares user choice and computer choice and determines the winner
    machine_choice()  # imports the machine choice

    if machine_choice() == 'p' and user_choice == 's':
        return 'Your scissor just ripped your opponent paper to shreds\nYou Won!'

    elif machine_choice() == 's' and user_choice == 'p':
        return 'Your opponent scissor just ripped your paper to shreds\nYou Lost!'
    elif machine_choice() == 'p' and user_choice == 'r':
        return 'Your opponent paper just wrapped your rock\nYou Lost!'
    elif machine_choice() == 'r' and user_choice == 'p':
        return 'Your paper just wrapped your opponent rock\nYou Won!'
    elif machine_choice() == 's' and user_choice == 'r':
        return 'Your rock just smashed your opponent scissor\nYou Won!'
    elif machine_choice() == 'r' and user_choice == 's':
        return 'Your opponent rock just smashed your scissor\nYou Lost!'
    elif machine_choice() == user_choice:
        return 'Tie All!'



def output():
    user_choice = input('Please make your decision\n'  # asks for user choice
                        'For paper insert: "p", '
                        'For rock insert: "r" and '
                        'For scissor insert: "s"\n')
    if resault(user_choice):    #If user insert an valid data
        print(resault(user_choice))         #runs the resault function
        continue_or_abord = input('Please select one of these:\n' #See if user wants to play again
                                  '1) play again\n'
                                  '2) exit\n')
        while continue_or_abord != '2':     #If user insert an invalid data
            if continue_or_abord == '1':
                return output()
            elif continue_or_abord == '2':
                print('Thank you and goodbye.')
            else:
                continue_or_abord = input('Please select one of above:\n')

        print('Thank you and goodbye.')
    else:                                   #if user insert an invalid data(neither of 'r', 's' or 'p'
        print('"'+user_choice+'"' + ' is not a valid choice!!')
        return output()
output()