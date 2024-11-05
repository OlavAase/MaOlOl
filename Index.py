###Her 

from Players import Spiller, Computers
from random import randint as rd

risktaker = Computers("The Risktaker", [0]*6, 1, 30)
print(risktaker.kast_terning())
print(risktaker)