#Her lager vi classene med spillerne og computerne
from random import randint as rd
from collections import Counter

class Spiller:
    def __init__(self, navn, antall_terninger, nummer, flest_av_terninger):
        self.navn = navn
        self.antall_terninger = antall_terninger
        self.nummer = nummer
        self.flest_av_terninger = flest_av_terninger

    def __str__(self):
        return f"Dette er {self.navn}, han har {len(self.antall_terninger)} terninger og er nummer {self.nummer} i rekka "

    def kast_terning(self):
        for i in range(len(self.antall_terninger)):
            self.antall_terninger[i] = (rd(1,6))
        return self.antall_terninger
    
    def telling_terning(self):
        for i in range(1, 7):
            self.flest_av_terninger = self.antall_terninger.count(i)
            print(self.flest_av_terninger)




class Computers(Spiller):
    def __init__(self, navn, antall_terninger, nummer, flest_av_terninger, spillmåte,):
        super().__init__(navn, antall_terninger, nummer, flest_av_terninger)
        self.spillmåte = spillmåte



