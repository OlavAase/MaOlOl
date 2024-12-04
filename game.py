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

#Gjette funksjon som passer på at du gjetter en terningside mellom 2 og 6 og at du enten tipper høyere terningside eller terning antall
    def guess(self, face, amount):  
        
        while face > 6 or face < 2: #Passer på at du tipper terningside mellom 2 og 6
            face = int(input("Fins ikke terningside du kan tippe på større en 6 eler mindre en 2. Hvilken terningside vil du tippe på? (1-6)"))
        
        if face <= self.current_guess["die_face"]:
            while amount <= self.current_guess["amount_of_dice"] or amount <= 0: 
                amount = int(input(f"Du må tippe et høyere antall terninger. Hvor mange {self.current_guess["die_face"]}ere tror du at det er?"))
        else:
            while amount < self.current_guess["amount_of_dice"] or amount <= 0: 
                amount = int(input(f"2Du må tippe et høyere antall terninger. Hvor mange {self.current_guess["die_face"]}ere tror du at det er?"))
        
        self.current_guess["die_face"] = face 
        self.current_guess["amount_of_dice"] = amount
                        
        return self.current_guess
        
        
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        return self.players[self.current_player_index]     
    

    #funkskjon for utfordringen
    def challenge(self):
        total_matching = sum(player.dice.count(self.current_guess["die_face"]) + player.dice.count(1) for player in self.players)
        challenger = self.players[self.current_player_index]
        
        #ser om utfordreren vinner
        if total_matching >= self.current_guess["amount_of_dice"]:
            challenger.loose_dice()  
            result = f"{challenger.name} Utfordret og mister en terning!"
            result = f"Det var {total_matching} av denne terningen! {challenger.name} utfordret og mister en terning!"
        else:
            previous_player_index = (self.current_player_index - 1) % len(self.players)
            self.players[previous_player_index].loose_dice()  
            result = f"{self.players[previous_player_index].name} ble utfordret og mister en terning!"
            result = f"Det var {total_matching} av denne terningen! {self.players[previous_player_index].name} ble utfordret og mister en terning!"
        return result
    
  
        

    #spør deg om du vil utfordre eller gjette 
    def action_output(self):
        challenge_happened = False
        if self.current_guess["die_face"] == 0 and self.current_guess["amount_of_dice"] == 0:
            face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
            amount = int(input("Hvor mange av den terningen tror du at det er?"))
            self.guess(face, amount)
        else:
            while True:
                action =  str(input("Vil du gjette høyere (G) eller utfordre (U)?")).lower()
                if action == "g" or action == "u":
                    if action == "g":
                        face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
                        amount = int(input("Hvor mange av den terningen tror du at det er?"))
                        print("player guess")
                        print(self.guess(face, amount)) 
                        break   
                    else:
                        print("Oi oi oi vi har en  utfordring!")
                        print(self.challenge())
                        challenge_happened = True
                        break
                print("Det du skrev ble ikke akseptert. Svar G eller U")


            return challenge_happened
               
            



