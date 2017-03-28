from random import randint
from collections import deque

CC1 = 1
CC2 = 17
CC3 = 33
CH1 = 7
CH2 = 22
CH3 = 36
GO = 0
JAIL = 10
G2J = 30

def move(pos):

    pos = pos % 40
    
    if pos == CC1 or pos == CC2 or pos == CC3:
        chance = randint(1,16)
        if chance == 1:
            pos = GO
        elif chance == 2:
            pos = JAIL
    elif pos == CH1 or pos == CH3 or pos == CH3:
        chance = randint(1,16)
        if chance == 1:
            pos = GO
        elif chance == 2:
            pos = JAIL
        elif chance == 3:
            pos = 11 # go to c1
        elif chance == 4:
            pos = 24 # go to e3
        elif chance == 5:
            pos = 39
        elif chance == 6:
            pos = 5
        elif chance == 7 or chance == 8:
            if pos == CH1:
                pos = 15
            elif pos == CH2:
                pos = 25
            elif pos == CH3:
                pos = 5
        elif chance == 9:
            if pos == CH1 or pos == CH3:
                pos = 12
            else:
                pos = 28
        elif chance == 10:
            pos -= 3
            pos = pos % 39
    elif pos == G2J:
        pos = JAIL
    return pos

pos = 0 # Initial player position
pos_freqs = [0 for _ in range(40)]
DIE = 4 # Max value on die
TRIALS = 1000000 # number of rolls to simulate

last_rolls = deque()
last_rolls.append(0)
last_rolls.append(0)
for _ in range(TRIALS):
    num_doubles = 0
    first = randint(1,DIE)
    second = randint(1,DIE)
    
    pos = move(pos+first+second)
    if first == second: # rolled doubles
        first = randint(1,DIE)
        second = randint(1,DIE)
        pos = move(pos+first+second)
        if first == second: # rolled doubles
            first = randint(1,DIE)
            second = randint(1,DIE)
            pos = move(pos+first+second)
            if first == second:
                pos = JAIL
    pos_freqs[pos] += 1



sorted_pos_freqs = sorted(pos_freqs)
sorted_pos_freqs = sorted_pos_freqs[::-1]
sorted_pos_idcs = [str(pos_freqs.index(p)) for p in sorted_pos_freqs]
print ''.join(sorted_pos_idcs[:3])
import pdb; pdb.set_trace() 
