import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards[:3])
    
    def __getitem__(self,position):
        return self._cards[position]

    def __repr__(self):
        return "this is repr {}".format(self._cards[0])




if __name__ == '__main__':
    fd = FrenchDeck()
    # ranks = fd.ranks
    # suits = fd.suits
    # print(ranks)
    # print(suits)
    print(len(fd))
    # print(fd[0])
    # from random import choice
    # print(choice(fd))
    # print(fd[:3])
    # print(fd[12::13])
    print(fd)


    
