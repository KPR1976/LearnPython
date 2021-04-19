'''
   |   |   
 1 | 2 | 3  
   |   |   
-----------
   |   |   
 4 | 5 | 6  
   |   |   
-----------
   |   |   
 7 | 8 | 9  
   |   |     

'''
symbols = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
finish = True

def display_board():
    
    for i in range(11):

            if i % 2 == 0:
                print('   |   |   ')
            elif i == 1:
                print(' ' + symbols[0] + ' | ' + symbols[1] + ' | ' + symbols[2] + ' ')
            elif i == 5:
                print(' ' + symbols[3] + ' | ' + symbols[4] + ' | ' + symbols[5] + ' ')
            elif i == 9:
                print(' ' + symbols[6] + ' | ' + symbols[7] + ' | ' + symbols[8] + ' ')
            else:
                print('-----------')            

print('Welcome to Tic Tac Toe!')
player1 = ''
while player1 not in ['X', 'O']:
    player1 = input('Player 1 - choose your side X or O:' ).upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'      

display_board()

for i in range(9):
    if i % 2 == 0:
        step = int(input('Player #1 choose a position 1-9: '))
        symbols[step-1] = 'X'
        display_board()
        if symbols[0] == symbols[1] == symbols[2] == 'X' or symbols[0] == symbols[4] == symbols[8] == 'X' or symbols[0] == symbols[3] == symbols[6] == 'X' or \
            symbols[3] == symbols[4] == symbols[5] == 'X' or symbols[6] == symbols[7] == symbols[8] == 'X' or symbols[1] == symbols[4] == symbols[7] == 'X' or \
                symbols[2] == symbols[5] == symbols[8] == 'X' or symbols[2] == symbols[4] == symbols[6] == 'X':
            print('You are winner Player #1!')
            break
    else:
        step = int(input('Player #2 choose a position 1-9: '))
        symbols[step-1] = 'O'
        display_board()
        if symbols[0] == symbols[1] == symbols[2] == 'O' or symbols[0] == symbols[4] == symbols[8] == 'O' or symbols[0] == symbols[3] == symbols[6] == 'O' or \
            symbols[3] == symbols[4] == symbols[5] == 'O' or symbols[6] == symbols[7] == symbols[8] == 'O' or symbols[1] == symbols[4] == symbols[7] == 'O' or \
                symbols[2] == symbols[5] == symbols[8] == 'O' or symbols[2] == symbols[4] == symbols[6] == 'O':
            print('You are winner Player #2!')
            break
    print('Tie game!')
    