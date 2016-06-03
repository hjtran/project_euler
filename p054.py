from time import time
start = time()
def cardTuple(txt):
    if txt[0] == 'T':
        return (10,txt[1])
    elif txt[0] == 'J':
        return (11,txt[1])
    elif txt[0] == 'Q':
        return (12,txt[1])
    elif txt[0] == 'K':
        return (13,txt[1])
    elif txt[0] == 'A':
        return (14,txt[1])
    else:
        return (int(txt[0]),txt[1])

class Hand:

    def __init__(self,cards):
        self._cards = cards
        self._cards.sort(key = lambda x:x[0],reverse=True)
        
        self._fullHouse = False
        self._4oaK = 0
        self._3oaK = 0
        self._pairs = []
        for i in range(2):
            if all([True if cards[j][0] == cards[j+1][0] else False for j in range(i,i+3)]):
                self._4oaK = cards[i][0]
                break
        else:
            for i in range(3):
                if all([True if cards[j][0] == cards[j+1][0] else False for j in range(i,i+2)]):
                    self._3oaK = cards[i][0]
                    if sum([1 for k in range(4) if cards[k][0]==cards[k+1][0]])==3:
                        self._fullHouse = True
                    break
            else:
                for i in range(4):
                    if cards[i][0] == cards[i+1][0]:
                        self._pairs.append(cards[i][0])
                self._pairs.sort(reverse=True)


        if all([True if cards[i][1]==cards[i+1][1] else False for i in range(4)]):
            self._flush = True
        else:
            self._flush = False

        if all([True if cards[i][0]==cards[i+1][0]+1 else False for i in range(4)]):
            self._straight = True
        else:
            self._straight = False

        if self._flush and self._straight and cards[0][0]==14:
            self._handrank = 10
        elif self._flush and self._straight:
            self._handrank = 9
        elif self._4oaK!=0:
            self._handrank = 8
        elif self._fullHouse:
            self._handrank = 7
        elif self._flush:
            self._handrank = 6
        elif self._straight:
            self._handrank = 5
        elif self._3oaK!=0:
            self._handrank = 4
        elif len(self._pairs) == 2:
            self._handrank = 3
        elif len(self._pairs) == 1:
            self._handrank = 2
        else:
            self._handrank = 1

    def beats(self,p2):
        if self._handrank > p2._handrank:
            return True
        elif self._handrank < p2._handrank:
            return False
        elif self._handrank == 8:
            if self._4oaK > p2._4oaK:
                return True
            else:
                return False
        elif self._handrank == 4:
            if self._3oaK > p2._3oaK:
                return True
            else:
                return False
        elif self._handrank == 3 :
            if self._pairs[0] > p2._pairs[0]:
                return True
            elif self._pairs[0] < p2._pairs[0]:
                return False
            elif self._pairs[1] > p2._pairs[1]:
                return True
            else:
                return False
        elif self._handrank == 2:
            if self._pairs[0] > p2._pairs[0]:
                return True
            else:
                return False

        else:
            for i in range(4):
                if self._cards[i][0] > p2._cards[i][0]:
                    return True
                elif self._cards[i][0] < p2._cards[i][0]:
                    return False

with open('inputs/p054.txt','r') as infile:
    count = 0
    for game in infile.readlines():
        game = game.split(' ')
        p1 = Hand([cardTuple(c) for c in game[:5]])
        p2 = Hand([cardTuple(c) for c in game[5:]])
        if p1.beats(p2):
            count += 1
print count
print 'Elapsed time: %.5f seconds' % (time()-start,)

