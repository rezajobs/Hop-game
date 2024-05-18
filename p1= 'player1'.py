player1 = 'Player 1'
player2 = 'Player 2'
counter = 1
is_running = True

score1= 3
score2= 3

player1_first_turn = True

while is_running:
    player = player1 if counter % 2 != 0 else player2
      
    while True:
        user_input= input(f'{player}:')
        if player == player1 and player1_first_turn:
            if user_input.startswith('1'):
                player1_first_turn = False
                break
            else:
                print("Player 1's first input must start with 1. Try again.")
        else:
            break

    if counter %5 == 0:
        if  user_input.lower == 'hop':
            print(user_input)
        else:
            if  counter % 2 == 0:
                score2 -= 1
                print(f'{player},new score is {score2}')
            else:
                score1-=1
                print(f'{player},new score is {score1}')

            if score1 == 0:
                print(f'{player1} loses')
                break
            elif score2 == 0:
                print(f"{player2} loses")
                break
    else:
        print(user_input)
        

    counter += 1
