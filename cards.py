import random
 
class Card:
 
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
 
    def __str__(self):
        return f'{self.rank} - {self.suit}'
       
 
class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        suits = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards) 
        
    def shu_ffle(self):
        return self.cards 
        
        
                
def main():
    d = Deck()
    print(*d.shu_ffle(),sep = '\n')
    
 
if __name__ == '__main__':
    main()