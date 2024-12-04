###Her 

from player import Player
from random import randint as rd
from game import Game
from gamestartfunksjon import gamestart

players = [
    Player("Player1", is_human = True,),
    Player("Computer", is_human = False, is_good= False),
    Player("Bot", is_human = False, is_good = True),
]
game = Game(players)



def gameloop():
    print("\n")

    game_ongoing = True
    round_ongoing = True
    spillrunde = 0
    gjett = 0
    while game_ongoing == True:
        for player in players:
            player.roll_dice()
            print(f"{player.name}'s dice: {player.show_dice()}")
        print("\n")
        round_ongoing = True
        spillrunde += 1
       
        
        

        while round_ongoing == True:
            print(
                "---------------------------------------------------------------\n"
                f"Det er spillrunde {spillrunde} og det har skjedd {gjett} gjett i den spillrunden\n"
                "---------------------------------------------------------------\n"
                )
            current_player = game.players[game.current_player_index]
            print(f"Det er {current_player.name} sin tur")
            print(f"Nåverende gjett er {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere\n")
            if current_player.is_human == True:
                print(f"Dette er {current_player.name} sine terninger: {current_player.dice}")
                challenged_happened = game.action_output()
                gjett += 1
                if challenged_happened:
                    gjett = 0
                    round_ongoing = False
                    game.current_guess  = {
                    "die_face": 0,
                    "amount_of_dice": 0,
        }
                    
                
            else:
                if game.current_guess["die_face"] == 0 and game.current_guess["amount_of_dice"] == 0:
                    game.guess(2, 1) 
                    gjett += 1
                    print(f"{current_player.name} gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere ")
                else:
                    if current_player.is_good == False:
                        computer_action = rd(1,2)
                    elif current_player.is_good:
                        if game.current_guess["amount_of_dice"] < (game.total_dice_left() / 3):
                            computer_action = 1
                    if computer_action == 1:
                        gjett += 1
                        amount_or_face = rd(1,2)
                        if amount_or_face == 1:
                            game.guess(game.current_guess["die_face"] + 1, game.current_guess["amount_of_dice"])
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                        else: 
                            game.guess(game.current_guess["die_face"], game.current_guess["amount_of_dice"] + 1)
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                    else:
                        print("Det ble utfordret!")
                        print(f"Dette var computer sine terninger: {current_player.dice}")
                        round_ongoing = False
                        print(game.challenge())
                        game.current_guess  = {
                        "die_face": 0,
                        "amount_of_dice": 0,
        }
            
                        
                        gjett = 0
                        
            print("\n")
            game.next_turn()
            

gamestart()
gameloop()