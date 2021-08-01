import random
import time

print(""" 
      Rock,paper,scissors game 
      please choose one of them
      1.Rock
      2.Paper 
      3.Scissors  
      4.Exit 
      """)  

while True:
    player_1= input("Enter name of player one:")
    str="{} choose your number:"
    user1=int(input(str.format(player_1)))
    
    
    if user1==4:
        print("Game Over!")
        break
    elif user1>=5:
        print("Invalid choice please choose 1 to 4")
        continue
    else:
        game={1:"rock",2:"paper",3:"scissors"}
        AI_1=random.randint(1,3)
        user_c1=game.get(user1)
        AI=game.get(AI_1)
        str2="{} win! i chose {} i loose"
        str3="{} loose i chose {} i win!"
        if user_c1=="rock" and AI=="scissors":
            time.sleep(0.1)
            print(str2.format(player_1,AI))
        elif user_c1=="rock" and AI=="paper":
            time.sleep(0.1)
            print(str3.format(player_1,AI))
        elif user_c1=="paper" and AI=="scissors":
            time.sleep(0.1)
            print(str3.format(player_1,AI))
        elif user_c1=="paper" and AI=="rock":
            time.sleep(0.1)
            print(str2.format(player_1,AI))
        elif user_c1=="scissors" and AI=="paper":
            time.sleep(0.1)
            print(str2.format(player_1,AI))
        elif user_c1=="scissors" and AI=="rock":
            time.sleep(0.1)
            print(str3.format(player_1,AI))
        else:
            print("the game was a draw,please continue")
            
            
