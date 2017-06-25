from time import time
from fractions import Fraction
start = time()

# Problem Code
P_dice = [Fraction(1,4)]*4
P_probs = [Fraction(1,4)]*4
for _ in range(8):
    new_P_probs = [0]*(len(P_probs)+5)
    for num1,prob1 in enumerate(P_probs):
        for num2,prob2 in enumerate(P_dice):
            num2+=1
            new_P_probs[num1+num2] += prob1*prob2
    P_probs = new_P_probs

C_dice = [Fraction(1,6)]*6
C_probs = [Fraction(1,6)]*6
for _ in range(5):
    new_C_probs = [0]*(len(C_probs)+7)
    for num1,prob1 in enumerate(C_probs):
        for num2,prob2 in enumerate(C_dice):
            num2+=1
            new_C_probs[num1+num2] += prob1*prob2
    C_probs = new_C_probs

s = 0
for idx,c in enumerate(C_probs):
    s += c*sum(P_probs[idx+1:])
    
print(float(s))

print('Time Elapsed: %.2fs' % (time()-start,))        
