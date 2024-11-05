###Her 

from Players import Spiller, Computers
from random import randint as rd

risktaker = Computers("The Risktaker", [0]*6, 1, 30, 0)
print(risktaker.kast_terning())
print(risktaker.telling_terning())