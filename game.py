class Game: 
    def __init__(self, players):
        self.players = players
        self.current_guess = {
            "die_face": 4,
            "amount_of_dice": 7,
        }

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


player1 = Game("player1")
print(player1.guess(6, 7))
