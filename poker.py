import sys


class Poker:

    carteMasa1 = ()
    carteMasa2 = ()
    carteMasa3 = ()
    carteMasa4 = ()
    carteMasa5 = ()

    carte1 = ()
    carte2 = ()

    def __init__(self, culoare1, valoare1, culoare2, valoare2):
        self.carte1 = (culoare1, valoare1)
        self.carte2 = (culoare2, valoare2)

    def cartiJucator(self):
        totalCartiJucator = []

        totalCartiJucator.append(Poker.carteMasa1)
        totalCartiJucator.append(Poker.carteMasa2)
        totalCartiJucator.append(Poker.carteMasa3)
        totalCartiJucator.append(Poker.carteMasa4)
        totalCartiJucator.append(Poker.carteMasa5)
        totalCartiJucator.append(self.carte1)
        totalCartiJucator.append(self.carte2)
        for iterator in totalCartiJucator:
            if iterator[1] == 1:
                totalCartiJucator.append((iterator[0], 14))

        return totalCartiJucator

    @staticmethod
    def verificaChintaDeCuloare(carti):
        
        
        
        pass

    @staticmethod
    def verificaCareu(carti):
        pass

    @staticmethod
    def verificaFullHouse(carti):
        pass

    @staticmethod
    def verificaCuloare(carti):
        pass

    @staticmethod
    def verificaChinta(carti):
        pass

    @staticmethod
    def verificaCui(carti):
        pass

    @staticmethod
    def verificaDouaPerechi(carti):
        pass

    @staticmethod
    def verificaPereche(carti):
        pass

    @staticmethod
    def verificaCarteMare(carti):
        pass

    def manaMaxima(self):

        manaJucator = self.cartiJucator()
        if Poker.verificaChintaDeCuloare(manaJucator):
            return Poker.verificaChintaDeCuloare(manaJucator)
        if Poker.verificaCareu(manaJucator):
            return Poker.verificaCareu(manaJucator)
        if Poker.verificaFullHouse(manaJucator):
            return Poker.verificaFullHouse(manaJucator)
        if Poker.verificaCuloare(manaJucator):
            return Poker.verificaCuloare(manaJucator)
        if Poker.verificaChinta(manaJucator):
            return Poker.verificaChinta(manaJucator)
        if Poker.verificaCui(manaJucator):
            return Poker.verificaCui(manaJucator)
        if Poker.verificaDouaPerechi(manaJucator):
            return Poker.verificaDouaPerechi(manaJucator)
        if Poker.verificaPereche(manaJucator):
            return Poker.verificaPereche(manaJucator)
        if Poker.verificaCarteMare(manaJucator):
            return Poker.verificaCarteMare(manaJucator)

        print("Nu a gasit mana")
        sys.exit


Poker.carteMasa1 = ("inima", 3)
Poker.carteMasa2 = ("inima", 2)
Poker.carteMasa3 = ("inima", 6)
Poker.carteMasa4 = ("frunza", 1)
Poker.carteMasa5 = ("trefla", 2)
jucator = Poker("inima", 4, "inima", 5)

lista=jucator.cartiJucator()
print(lista[5])
print(jucator.cartiJucator())
print(jucator.manaMaxima())
