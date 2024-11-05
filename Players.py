#Her lager vi classene med spillerne og computerne
from random import randint as rd
class Spiller:
    def __init__(self, navn, antall_terninger, nummer):
        self.navn = navn
        self.antall_terninger = antall_terninger
        self.nummer = nummer

    def __str__(self):
        return f"Dette er {self.navn}, han har {len(self.antall_terninger)} terninger og er nummer {self.nummer} i rekka "

    def kast_terning(self):
        self.antall_terninger = []
        for i in range(6):
            self.antall_terninger.append(rd(1,6))
        return self.antall_terninger




class Computers(Spiller):
    def __init__(self, navn, antall_terninger, nummer, spillmåte):
        super().__init__(navn, antall_terninger, nummer)
        self.spillmåte = spillmåte





risktaker = Computers("The Risktaker", [0]*6, 1, 30)
print(risktaker.kast_terning())
print(risktaker)

