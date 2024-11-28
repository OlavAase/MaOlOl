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
            challenger.loose_dice()  
            result = f"{challenger.name} challenged and loses a die!"
            result = f"Det var {total_matching} av denne terningen! {challenger.name} challenga og mister en terning!"
        else:
            previous_player_index = (self.current_player_index - 1) % len(self.players)
            self.players[previous_player_index].loose_dice()  
            result = f"{self.players[previous_player_index].name} got challenged and loses a die!"
            result = f"Det var {total_matching} av denne terningen! {self.players[previous_player_index].name} ble challenga og mister en terning!"
        return result
    
  
        

    
       
    def action_output(self):
        challenge_happened = False
        if self.current_guess["die_face"] == 0 and self.current_guess["amount_of_dice"] == 0:
            face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
            amount = int(input("Hvor mange av den terningen tror du at det er?"))
            self.guess(face, amount)
        else:
            action =  str(input("Do you want to guess (G) or challenge (C)?")).lower()
            if action == "g" or action == "c":
                if action == "g":
                    face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
                    amount = int(input("Hvor mange av den terningen tror du at det er?"))
                    print("player guess")
                    self.guess(face, amount)
                    
                else:
                    print("challenge")
                    print(self.challenge())
                    challenge_happened = True
            return challenge_happened
               
            



