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
        return f"Dette er {self.navn}, han har {len(self.antall_terninger)} terninger og er nummer {self.nummer} i rekka og han har flest {self.flest_av_terninger}"

    def kast_terning(self):
        for i in range(len(self.antall_terninger)):
            self.antall_terninger[i] = (rd(1,6))
        return self.antall_terninger
    
    def telling_terning(self):
        antall_av_terning = 0 #variabel som lagrer hvor mange det tallet det er flest av
        for i in range(2, 7): #teller alle tall utenom 1
            print(self.antall_terninger.count(i)) # printer hvor mange av hvert tall det er
            if self.antall_terninger.count(i) >= antall_av_terning: 
                antall_av_terning = self.antall_terninger.count(i) #oppdaterer hvor mange det tallet som er flest er
                self.flest_av_terninger = i #lagrer hvilket tall det er flest av
        return f"Det er flest {self.flest_av_terninger}ere og det er {self.antall_terninger.count(self.flest_av_terninger) + self.antall_terninger.count(1)} {self.flest_av_terninger}ere" #returnerer det tallet det er flest av og legger til enere
        




class Computers(Spiller):
    def __init__(self, navn, antall_terninger, nummer, flest_av_terninger, spillmåte,):
        super().__init__(navn, antall_terninger, nummer, flest_av_terninger)
        self.spillmåte = spillmåte



