game_list = [0,1,2]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

display_game(game_list)

def position_choice():
    choice = 'wrong'

    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0','1', '2']:
            print ("Sorry, invalid choice! ")

    return int(choice)

position_choice()

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

replacement_choice(game_list,1)

def gameon_choice():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        
        if choice not in ['Y','N']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            
            
            print("Sorry, I didn't understand. Please make sure to choose Y or N.")
            
    
    # Optionally you can clear everything after running the function
    # clear_output()
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False

gameon_choice()

# Variable to keep game playing
game_on = True

# First Game List
game_list = [0,1,2]



while game_on:
    #Display information
    display_game(game_list)
    #Getting user information
    position = position_choice()
    #Update what we are displaying
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    #Getting more user information
    game_on = gameon_choice()

