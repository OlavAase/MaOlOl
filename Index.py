###Her 

from player import Player
from random import randint as rd
from game import Game
from gamestartfunksjon import gamestart

players = [
    Player("Player1", is_human = True),
    Player("Computer", is_human = False),
]
game = Game(players)



def gameloop():
    print("\n")

    game_ongoing = True
    round_ongoing = True
    while game_ongoing == True:
        for player in players:
            player.roll_dice()
            print(f"{player.name}'s dice: {player.show_dice()}")
        print("\n")
        round_ongoing = True
       
        
        

        while round_ongoing == True:
            
            current_player = game.players[game.current_player_index]
            print(f"Det er {current_player.name} sin tur")
            print(f"Nåverende gjett er {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
            if current_player.is_human == True:
                challenged_happened = game.action_output()
                if challenged_happened:
                    round_ongoing = False
                    game.current_guess  = {
                    "die_face": 0,
                    "amount_of_dice": 0,
        }
            else:
                if game.current_guess["die_face"] == 0 and game.current_guess["amount_of_dice"] == 0:
                    game.guess(2, 1) 
                else:
                    computer_action = rd(1,2)
                    if computer_action == 1:
                        amount_or_face = rd(1,2)
                        if amount_or_face == 1:
                            game.guess(game.current_guess["die_face"] + 1, game.current_guess["amount_of_dice"])
                            print(f"Computer gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                        else: 
                            game.guess(game.current_guess["die_face"], game.current_guess["amount_of_dice"] + 1)
                            print(f"Computer gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                    else:
                        print("Computer challenger")
                        round_ongoing = False
                        print(game.challenge())
                        game.current_guess  = {
                        "die_face": 0,
                        "amount_of_dice": 0,
        }
                        
            print("\n")
            game.next_turn()
            

gamestart()
gameloop()