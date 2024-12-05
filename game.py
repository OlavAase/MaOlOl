from player import Player
from random import randint as rd
import time

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
        while True:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            if self.players[self.current_player_index].dice_count > 0:  # Hopper over spillere uten terninger
                break
        return self.players[self.current_player_index]
    
       #funkskjon for utfordringen
    def challenge(self):
        total_matching = sum(player.dice.count(self.current_guess["die_face"]) + player.dice.count(1) for player in self.players)
        challenger = self.players[self.current_player_index]
        
        #sjekker om antallet av den bestemte terningen er større eller lik hva som ble gjettet og gir resultat etter hvem som vinner utfordringen
        if total_matching >= self.current_guess["amount_of_dice"]:
            challenger.loose_dice()
            result = f"Det var {total_matching} av denne terningen! {challenger.name} utfordret og mister en terning!"
        else:
            previous_player_index = (self.current_player_index - 1) % len(self.players)
            self.players[previous_player_index].loose_dice()  
            result = f"Det var {total_matching} av denne terningen! {self.players[previous_player_index].name} ble utfordret og mister en terning!"
        return result
    
  
        

    
          #funksjon for å la brukeren gjette antall av en bestemt terning
    def action_output(self):
        challenge_happened = False
        if self.current_guess["die_face"] == 0 and self.current_guess["amount_of_dice"] == 0:
            face = int(input("Hvilken terningside vil du tippe på? (1-6)"))
            amount = int(input("Hvor mange av den terningen tror du at det er?"))
            self.guess(face, amount)
        else:
            #dersom det har blitt gjettet før, får du muligheten til å gjette høyere eller utfordre
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
                        time. sleep(2)
                        print(self.challenge())
                        challenge_happened = True
                        break
                print("Det du skrev ble ikke akseptert. Svar G eller U")


            return challenge_happened
               
#definerer spillere hentet fra player.py og sier om de er mennesker eller datamaskiner     
players = [
    Player("Player1", is_human = True,),
    Player("Computer", is_human = False, is_good= False),
    Player("Bot", is_human = False, is_good = True),
]
game = Game(players)

#selve systemet for rundene i spillet
def gameloop():
    print("\n")

    game_ongoing = True
    round_ongoing = True
    spillrunde = 0
    gjett = 0
    #når runden starter trilles terningene og brukeren får oppgitt sine terninger
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
            #time. sleep() er en måte å delaye hva som printes i terminalen. noe som gjør det lettere for spilleren å få med seg hva som skjer i spillet.
            time. sleep(2)
            current_player = game.players[game.current_player_index]
            print(f"Det er {current_player.name} sin tur")
            print(f"Nåverende gjett er {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere\n")
            if current_player.is_human == True:
                print(f"Dette er {current_player.name} sine terninger: {current_player.dice}")
                time. sleep(2)
                challenged_happened = game.action_output()
                gjett += 1

                #avslutter runden dersom det har skjedd en utfordring
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
                    time. sleep(1)
                    print(f"{current_player.name} gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere ")
                else:
                    #is_good brukes for å skille mellom datamaskinene som er med i spillet og spillestilene deres
                    if current_player.is_good == False:
                        #dersom boten ikke er god tar den et tilfeldig valg om å gjette eller utfordre.
                        computer_action = rd(1,2)
                    elif current_player.is_good:
                        #den "gode" boten gjetter kun dersom det nåværende gjettet av antallet til terningen er mindre enn en tredjedel av alle terningene som fortsatt er med i spillet.
                        if game.current_guess["amount_of_dice"] < (game.total_dice_left() / 3):
                            computer_action = 1
                    #action 1 er å gjette
                    if computer_action == 1:
                        gjett += 1
                        amount_or_face = rd(1,2)
                        #forhindrer at botene ikke ka gjette ett høyere antall enn 6 på terningen
                        if amount_or_face == 1 and game.current_guess["die_face"] < 6:
                            game.guess(game.current_guess["die_face"] + 1, game.current_guess["amount_of_dice"])
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                        else: 
                            game.guess(game.current_guess["die_face"], game.current_guess["amount_of_dice"] + 1)
                            print(f"Det ble gjetta {game.current_guess["amount_of_dice"]} {game.current_guess["die_face"]}ere")
                    else:
                        print("Det ble utfordret!")
                        time. sleep(2)
                        for player in players:
                            print(f"Dette var {player.name} sine terninger: {player.dice}")
                            time. sleep(2)
                        round_ongoing = False
                        print(game.challenge())
                        game.current_guess  = {
                        "die_face": 0,
                        "amount_of_dice": 0,
        }
            
                        
                        gjett = 0
                        
            print("\n")
            #knapp for å gå til nestemann i køen. gjør spillet mer oversiktlig for brukeren
            neste = input("trykk på (n) for å gå videre til nestemann")
            if neste == "n":
                game.next_turn()
 


