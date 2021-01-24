'''
Tic Tac Toe game
'''

def desc(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    #Initial conditions
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False


    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number (0-10): ')

        #check isdigit
        if choice.isdigit() == False:
            print("Sorry, but we work only with digits!")
        #check range
        else:
            if int(choice) in acceptable_range:                
                within_range = True
            else:
                print('Sorry, you are out of acceptable range (0-10)')
                within_range = False

    return int(choice)              

def position_choice():
    
    # This original choice value can be anything that isn't an integer
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['0','1','2']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Pick a position to replace (0,1,2): ")
        
        if choice not in ['0','1','2']:
            # THIS CLEARS THE CURRENT OUTPUT BELOW THE CELL
            clear_output()
            
            print("Sorry, but you did not choose a valid position (0,1,2)")
    
    # We can convert once the while loop above has confirmed we have a digit.
    return int(choice)


def replacement_choice(game_list,position):
    
    user_placement = input("Type a string to place at the position")
    
    game_list[position] = user_placement
    
    return game_list    


'''
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
desc(row1, row2, row3)'''
print(user_choice())