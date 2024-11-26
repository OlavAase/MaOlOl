from random import randint as rd

class Player:
    def __init__(self, name, dice_count=5, is_human=True):
        self.name = name
        self.dice_count = dice_count
        self.dice = [0]*dice_count
        self.is_human = is_human
    
    def roll_dice(self):
        for i in range(self.dice_count):
            self.dice[i] = rd(1,6)
        
    
    def loose_dice(self):
        if self.dice_count > 0:
            self.dice_count -= 1
            self.dice.pop()
        return self.dice_count

    def show_dice(self):
        if self.is_human == True:
            return self.dice
        else:
            return self.dice

    

testplayer = Player("Test spiller", 1)
print(testplayer.roll_dice())
print(testplayer.show_dice())
print(testplayer.loose_dice())

        

        
