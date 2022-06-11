from random import random


print("let's play Rock Paper Scissors \n")
"choose R for rock \n"
"choose P for paper \n"
"choose S for scissors \n"
while True:
    game_options=["R", "S", "P"]
    computer = random.choices(game_options)
    player = None
    
    while player not in game_options:
        
        player=input("what do you choose: ")
        if player not in game_options:
            print("invalid input, try again")
        else:
            print("You", player)
            print("computer", computer)
            if player == computer:
                print("its a tie")
                continue
            elif player=="R":
                if computer =="S":
                 print(" Rock breaks scissors, you win")
                if computer=="P":
                    print("paper covers rock, you lose")
            elif player=="S":
                if computer=="P":
                    print("scissors cuts paper, you win")
                if computer =="R":
                    print("rock breaks scissors, you lose")
            elif player =="P":
                if computer=="S":
                    print("Scissors cuts paper, you lose")
                if computer=="R":
                        print("paper covers rock, you win")
            break
                    