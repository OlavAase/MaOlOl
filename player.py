from random import randint as rd


#objektorientering for å gi en spiller egenskaper
class Player:
    def __init__(self, name, dice_count=5, is_human=True, is_good = True,):
        self.name = name
        self.dice_count = dice_count
        self.dice = [0]*dice_count
        self.is_human = is_human
        self.is_good = is_good
    
    #funskjon for å trille terning
    def roll_dice(self):
        for i in range(self.dice_count):
            self.dice[i] = rd(1,6)
        
    #funskjon for å miste en terning dersom man taper en runde
    def loose_dice(self):
        if self.dice_count > 0:
            self.dice_count -= 1
            self.dice.pop()
        return self.dice_count

    #denne funksjonen viser terningene dine, men skjuler motstanderne dine sine terninger slik at du faktisk må gjette, din juksemaker.
    def show_dice(self):
        if self.is_human == True:
            return self.dice
        else:
            return "Computer terninger er gjemt"

    

        

        
