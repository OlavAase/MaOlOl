###Her 

from Players import Spiller, Computers
from random import randint as rd

risktaker = Computers("The Risktaker", [0]*5, 1, 0, 30)
print(risktaker.kast_terning())
print(risktaker.telling_terning())
print(risktaker)

