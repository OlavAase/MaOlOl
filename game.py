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

    def total_dice_left(self):
        total_dice = sum(player.dice_count for player in self.players)
        return total_dice

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
        
        if total_matching >= self.current_guess["amount_of_dice"]:
            challenger.loose_dice()
            result = f"Det var {total_matching} av denne terningen! {challenger.name} utfordret og mister en terning!"
        else:
            previous_player_index = (self.current_player_index - 1) % len(self.players)
            self.players[previous_player_index].loose_dice()  
            result = f"Det var {total_matching} av denne terningen! {self.players[previous_player_index].name} ble utfordret og mister en terning!"
        return result
    
  
        

    
          #ser om utfordreren vinner
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
                        print("oi oi oi vi har en utfordring")
                        print(self.challenge())
                        challenge_happened = True
                        break
                print("Det du skrev ble ikke akseptert. Svar G eller U")


            return challenge_happened
               
            
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
                        if amount_or_face == 1 and game.current_guess["die_face"] < 6:
                            game.guess(game.current_guess["die_face"] + 1, game.current_guess["amount_of_dice"])
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                        else: 
                            game.guess(game.current_guess["die_face"], game.current_guess["amount_of_dice"] + 1)
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                    else:
                        print("Det ble utfordret!")
                        for player in players:
                            print(f"Dette var {player.name} sine terninger: {player.dice}")
                        round_ongoing = False
                        print(game.challenge())
                        game.current_guess  = {
                        "die_face": 0,
                        "amount_of_dice": 0,
        }
            
                        
                        gjett = 0
                        
            print("\n")
            game.next_turn()
 


