class Rank:
    def __init__ (self, symbol):
        self.symbol = symbol
        
class Suit:
    def __init__(self, color):
        self.color = color

        
symbols = ['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
colors = ['red','black']
RANKS = {ch : Suit(ch).__class__ for ch in symbols}