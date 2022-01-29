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
                return (vectValori[i], "ChintaDeCuloare")

    @staticmethod
    def verificaCareu(carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1

        if vectFrecv.count(4):
            return (vectFrecv.index(4), "Careu")

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

        return (trei, doi, "FullHouse")

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
                return (vectMaxCulori[it1], "Culoare")

    @staticmethod
    def verificaChinta(carti):
        vectValori = []

        for iterator in carti:
            vectValori.append(iterator[1])
        vectValori.sort()

        for i in range(len(vectValori) - 1, 3, -1):
            if vectValori[i-1] == vectValori[i]-1 and vectValori[i-2] == vectValori[i]-2 and vectValori[i-3] == vectValori[i]-3 and vectValori[i-4] == vectValori[i]-4:
                return (vectValori[i], "Chinta")

    @staticmethod
    def verificaCui(carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1

        for i in range(len(vectFrecv) - 1, 0, -1):
            if vectFrecv[i] == 3:
                return (i, "Cui")

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
                return(val1, i, "DouaPerechi")

    @staticmethod
    def verificaPereche(carti):
        vectFrecv = [0]*15

        for iterator in carti:
            vectFrecv[iterator[1]] += 1
        vectFrecv[1] = 0

        if vectFrecv.count(2) > 0:
            vectFrecv.reverse()
            print(vectFrecv)
            return (abs(vectFrecv.index(2)-14), abs(vectFrecv.index(1)-14), "Pereche")

    def verificaCarteMare(self):
        if self.carte1[1] > self.carte2[1]:
            return (self.carte1[1], "CarteMare")
        else:
            return (self.carte2[1], "CarteMare")

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
        if self.verificaCarteMare():
            return self.verificaCarteMare()

        print("Nu a gasit mana")
        sys.exit


Poker.carteMasa1 = ("trefla", 1)
Poker.carteMasa2 = ("romb", 9)
Poker.carteMasa3 = ("romb", 4)
Poker.carteMasa4 = ("inima", 13)
Poker.carteMasa5 = ("trefla", 11)
jucator = Poker("inima", 7, "inima", 5)

lista = jucator.cartiJucator()

print(jucator.cartiJucator())
print(jucator.manaMaxima())
