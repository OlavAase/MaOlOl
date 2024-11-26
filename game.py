from player import Player
from random import randint as rd

class Game: 
    def __init__(self, players):
        self.players = players
        self.current_guess = {
            "die_face": 0,
            "amount_of_dice": 0,
        }
        self.current_player_index = 0

    def guess(self, face, amount):
        if face > self.current_guess["die_face"] or amount > self.current_guess["amount_of_dice"]:
            if face <= 6:
                self.current_guess["die_face"] = face
            else:
                return "Ingen terningside er større en 6"
            self.current_guess["amount_of_dice"] = amount
            return self.current_guess
        else:
            return "Ble ikke akseptert"
        
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.players[self.current_player_index]     
    
    def challenge(self):
        total_matching = sum(player.dice.count(self.current_guess["die_face"]) + player.dice.count(1) for player in self.players)
        challenger = self.players[self.current_player_index]
        
        if total_matching >= self.current_guess["amount_of_dice"]:
            challenger.loose_dice()  # Fixed method name to "loose_dice" instead of "lose_dice"
            result = f"{challenger.name} challenged and loses a die!"
        else:
            previous_player_index = (self.current_player_index - 1) % len(self.players)
            self.players[previous_player_index].loose_dice()  # Fixed method name to "loose_dice"
            result = f"{self.players[previous_player_index].name} got challenged and loses a die!"
        return result
players = [
    Player("player1", is_human=True),
    Player("computer", is_human=False)
]
game = Game(players)

"""
for player in players:
        player.roll_dice()
        print(f"{player.name}'s dice: {player.show_dice()}")
current_player = game.players[game.current_player_index]
print(current_player.name)
print(game.guess(6, 7))
game.next_turn()
print(game.challenge())
"""

var = True
runde = True
while var == True:
    for player in players:
        player.roll_dice()
        print(f"{player.name}'s dice: {player.show_dice()}")
    runde = True
    game.current_guess  = {
            "die_face": 0,
            "amount_of_dice": 0,
        }

    
    while runde == True:
        game.next_turn()
        current_player = game.players[game.current_player_index]
        #print(current_player.name)
        if current_player.is_human == True:
            action = str(input("Do you want to guess (G) or challenge (C)?")).lower()
            if action == "g":
                face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
                amount = int(input("Hvor mange av den terningen tror du at det er?"))
                game.guess(face, amount)
            else:
                print(game.challenge())
                runde = False
        else:       
            if game.current_guess["die_face"] == 0 and game.current_guess["amount_of_dice"] == 0:
                # Ensure the computer doesn't guess before the human makes a valid guess
                game.guess(2, 1)  # Default first guess by the computer
            else:
                computer_action = rd(1,2)
                if computer_action == 1:
                    amount_or_face = rd(1,2)
                    if amount_or_face == 1:
                        game.guess(game.current_guess["die_face"] + 1, game.current_guess["amount_of_dice"])
                    else: 
                        game.guess(game.current_guess["die_face"], game.current_guess["amount_of_dice"] + 1)
                else:
                    print(game.challenge())
                    runde = False
            
        print(game.current_guess)



    
    #for player in players:
        #print(f"{player.name}'s dice: {player.show_dice()}")

    




    


"""
print(game.current_player_index)
current_player = game.players[game.current_player_index]
print(current_player.name)
print(sum(player.dice.count(game.current_guess["die_face"]) + player.dice.count(1) for player in game.players))

game.next_turn()
print(game.current_player_index)
game.next_turn()
print(game.current_player_index)
game.next_turn()
print(game.current_player_index)
game.next_turn()
print(game.current_player_index)

var = True
while var == True:
   
    for player in players:
        player.roll_dice()
        print(f"{player.name}'s dice: {player.show_dice()}")




    var = False
"""

