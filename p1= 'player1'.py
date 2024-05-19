player1 = 'Player 1'
player2 = 'Player 2'
level = 1
is_running = True

score1 = 3
score2 = 3

while is_running:
    player = player1 if level % 2 != 0 else player2
    
    user_input = input(f'{player}: ')
    
    if level % 5 == 0:
        if user_input.lower() == 'hop':
            print(user_input)
        else:
            print('error')
            if player == player1:
                score1 -= 1
                print(f'{player}, new score is {score1}')
            else:
                score2 -= 1
                print(f'{player}, new score is {score2}')
            
            if score1 == 0:
                print(f'{player1} loses')
                is_running = False
                break
            elif score2 == 0:
                print(f'{player2} loses')
                is_running = False
                break
    else:
        if str(level) == user_input:
            print(user_input)
        else:
            print('error')
            if player == player1:
                score1 -= 1
                print(f'{player}, new score is {score1}')
            else:
                score2 -= 1
                print(f'{player}, new score is {score2}')
            
            if score1 == 0:
                print(f'{player1} loses')
                is_running = False
                break
            elif score2 == 0:
                print(f'{player2} loses')
                is_running = False
                break

    level += 1
