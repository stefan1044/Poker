import sys
import random


class Poker:

    carteMasa1 = ()
    carteMasa2 = ()
    carteMasa3 = ()
    carteMasa4 = ()
    carteMasa5 = ()

    carte1 = ()
    carte2 = ()

    cartiFolosite = []
    listaCulori = ["inima", "romb", "trefla", "frunza"]

    def __init__(self, culoare1, valoare1, culoare2, valoare2):
        self.carte1 = (culoare1, valoare1)
        self.carte2 = (culoare2, valoare2)

    @staticmethod
    def alegeCarteRandom():

        while True:
            valoare = random.randint(1, 13)
            culoare = random.choice(Poker.listaCulori)
            if Poker.cartiFolosite.count((culoare, valoare)) == 0:
                Poker.cartiFolosite.append((culoare, valoare))
                return (culoare, valoare)

    def reseteazaCartiFolosite():
        Poker.cartiFolosite.clear()

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
        vectFrecvCulori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}
        vectValori = []
        culoare = 0

        for iterator in carti:
            if iterator[0] == "inima" or "romb" or "frunza" or "trefla" and iterator[1] != 14:
                vectFrecvCulori[iterator[0]] += 1

        for (it1, it2) in vectFrecvCulori.items():
            if it2 > 4:
                culoare = it1
        if culoare == 0:
            return None

        for iterator in carti:
            if iterator[0] is culoare:
                vectValori.append(iterator[1])
        vectValori.sort()

        for i in range(len(vectValori) - 1, 3, -1):
            if vectValori[i-1] == vectValori[i]-1 and vectValori[i-2] == vectValori[i]-2 and vectValori[i-3] == vectValori[i]-3 and vectValori[i-4] == vectValori[i]-4:
                return (8, vectValori[i], "ChintaDeCuloare")

    @staticmethod
    def verificaCareu(carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1

        if vectFrecv.count(4):
            return (7, vectFrecv.index(4), "Careu")

    @staticmethod
    def verificaFullHouse(carti):
        vectFrecv = [0]*15
        trei = None
        doi = None

        for iterator in carti:
            vectFrecv[iterator[1]] += 1
        vectFrecv[1] = 0

        for i in range(len(vectFrecv)-1, -1, -1):
            if vectFrecv[i] == 3:
                trei = i
                break
        if trei is None:
            return

        for i in range(len(vectFrecv)-1, -1, -1):
            if vectFrecv[i] == 2:
                doi = i
                break
        if doi is None:
            return

        return (6, trei, doi, "FullHouse")

    @staticmethod
    def verificaCuloare(carti):
        vectFrecvCulori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}
        vectMaxCulori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}

        for iterator in carti:
            if iterator[1] != 14:
                vectFrecvCulori[iterator[0]] += 1
            if iterator[1] > vectMaxCulori[iterator[0]]:
                vectMaxCulori[iterator[0]] = iterator[1]

        for (it1, it2) in vectFrecvCulori.items():
            if it2 > 4:
                return (5, vectMaxCulori[it1], "Culoare")

    @staticmethod
    def verificaChinta(carti):
        vectValori = []

        for iterator in carti:
            vectValori.append(iterator[1])
        vectValori.sort()

        for i in range(len(vectValori) - 1, 3, -1):
            if vectValori[i-1] == vectValori[i]-1 and vectValori[i-2] == vectValori[i]-2 and vectValori[i-3] == vectValori[i]-3 and vectValori[i-4] == vectValori[i]-4:
                return (4, vectValori[i], "Chinta")

    @staticmethod
    def verificaCui(carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1

        for i in range(len(vectFrecv) - 1, 0, -1):
            if vectFrecv[i] == 3:
                return (3, i, "Cui")

    @staticmethod
    def verificaDouaPerechi(carti):
        vectFrecv = [0]*15
        val1 = None

        for iterator in carti:
            vectFrecv[iterator[1]] += 1
        vectFrecv[1] = 0

        if vectFrecv.count(2) < 2:
            return None

        for i in range(len(vectFrecv)-1, -1, -1):
            if vectFrecv[i] == 2 and val1 is None:
                val1 = i
            elif vectFrecv[i] == 2:
                return(2, val1, i, "DouaPerechi")

    def verificaPereche(self, carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1
        vectFrecv[1] = 0

        if self.carte1[1] > self.carte2[1]:
            kicker = self.carte1
        else:
            kicker = self.carte2

        if vectFrecv.count(2) > 0:
            vectFrecv.reverse()
            return (1, abs(vectFrecv.index(2)-14), kicker[1], "Pereche")

    def verificaCarteMare(self):
        if self.carte1[1] > self.carte2[1]:
            return (self.carte1[1], "CarteMare")
        else:
            return (0, self.carte2[1], "CarteMare")

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
        if self.verificaPereche(manaJucator):
            return self.verificaPereche(manaJucator)
        if self.verificaCarteMare():
            return self.verificaCarteMare()

        print("Nu a gasit mana")
        sys.exit


for i in range(1, 30):
    Poker.carteMasa1 = Poker.alegeCarteRandom()
    Poker.carteMasa2 = Poker.alegeCarteRandom()
    Poker.carteMasa3 = Poker.alegeCarteRandom()
    Poker.carteMasa4 = Poker.alegeCarteRandom()
    Poker.carteMasa5 = Poker.alegeCarteRandom()

    cul1, val1 = Poker.alegeCarteRandom()
    cul2, val2 = Poker.alegeCarteRandom()
    jucator1 = Poker(cul1, val1, cul2, val2)

    cul1, val1 = Poker.alegeCarteRandom()
    cul2, val2 = Poker.alegeCarteRandom()
    jucator2 = Poker(cul1, val1, cul2, val2)

    j1 = jucator1.manaMaxima()
    j2 = jucator2.manaMaxima()
    print(f"Carti Masa:{Poker.carteMasa1} {Poker.carteMasa2} {Poker.carteMasa3} {Poker.carteMasa4} {Poker.carteMasa5} \nCarti jucator1: {jucator1.carte1} {jucator1.carte2} \nCarti jucator2: {jucator2.carte1} {jucator2.carte2} \n")
    print(f"Mana maxima Jucator1:{j1}\nMana maxima Jucator2:{j2}\n")

    Poker.reseteazaCartiFolosite()


''' Test Egalitate Random
totalCuloare= {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}
totalValori=[0]*14
for i in range (1,100000):
    Poker.carteMasa1=Poker.alegeCarteRandom()
    totalCuloare[Poker.carteMasa1[0]]+=1
    totalValori[Poker.carteMasa1[1]]+=1
print(f"Inima: {totalCuloare['inima']}\nRomb: {totalCuloare['romb']}\nFrunza: {totalCuloare['frunza']}\nTrefla: {totalCuloare['trefla']}")
contor=1
for i in totalValori:
    print(contor,end="  ")
    contor+=1
print('/n')
for i in totalValori:
    print(i,end=' ')
'''
