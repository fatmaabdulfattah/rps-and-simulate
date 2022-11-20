#rock paper scissors

import random 

#chekc who win
def get_winner(player,pc):
    #r>s s>p p>r
    if (player=='r' and pc=='s') or (player=='s' and pc=='p') or (player=='p' and pc=='r'):
        return True

rounds=int(input('How many turns you want? ')) 

#counter for each round
tie=0
pc_win=0
player_win=0

for i in range(rounds):
    player=input("choose one: 'r' for rock, 'p' for paper, 's' for scissors: ")
    pc=random.choice(['r','p','s']) 
    
    if player==pc:
        print("It's a tie!")
        tie+=1
        
    else:
        if get_winner(player,pc):
            print('You win!')
            player_win+=1
        else:
            print('You lose!')
            pc_win+=1
            
    print('score for now pc:'+str(pc_win)+' player:'+str(i+1-tie-pc_win))
