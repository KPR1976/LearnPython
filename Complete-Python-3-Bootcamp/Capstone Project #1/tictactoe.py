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

'''
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
desc(row1, row2, row3)'''
print(user_choice())