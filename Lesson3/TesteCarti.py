class Rank:
    def __init__ (self, symbol):
        self.symbol = symbol
    def __getattribute__ (self):
        print('fuiuuuuuuuuuuuuuuuuuck')
        return symbol

class Suit:
    def __init__(self, color):
        self.color = color

        
symbols = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
colors = ['red','black']
#RANKS = {ch : Suit(ch).__class__ for ch in symbols}

class Ace(Rank):
    pass
class King(Rank):
    pass
class Queen(Rank):
    pass
class Jack(Rank):
    pass
class Ten(Rank):
    pass
class Nine(Rank):
    pass
class Eight(Rank):
    pass
class Seven(Rank):
    pass
class Six(Rank):
    pass
class Five(Rank):
    pass
class Four(Rank):
    pass
class Three(Rank):
    pass
class Two(Rank):
    pass

RANKS = {'Ace' : Ace('Ace').__class__,'King' : King('King').__class__,
         'Queen' : Queen('Queen').__class__,'Jack' : Jack('Jack').__class__,
         'Ten' : Ten('Ten').__class__,'Nine' : Nine('Nine').__class__, 
         'Eight' : Eight('Eight').__class__ , 'Seven' : Seven('Seven').__class__,
         'Six' : Six('Six').__class__, 'Five' : Five('Five').__class__, 
         'Four' : Four('Four').__class__, 'Three' : Three('Three').__class__,
         'Two' : Two('Two').__class__}

class Hearts(Suit):
    pass
class Spades(Suit):
    pass
class Clubs(Suit):
    pass
class Diamonds(Suit):
    pass
    
SUITS = {'Hesrts':Hearts('red').__class__,'Spades':Spades('black').__class__,
         'Clubs':Clubs('black').__class__,'Diamods':Diamonds('red').__class__,}

print(RANKS)
print(SUITS)


