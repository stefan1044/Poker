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

    def __init__(self, culoare1, valoare1, culoare2, valoare2):
        self.carte1 = (culoare1, valoare1)
        self.carte2 = (culoare2, valoare2)

    @staticmethod
    def alege_carte_random():
        listaCulori = ["inima", "romb", "trefla", "frunza"]
        
        while True:
            valoare = random.randint(1, 13)
            culoare = random.choice(listaCulori)
            if Poker.cartiFolosite.count((culoare, valoare)) == 0:
                Poker.cartiFolosite.append((culoare, valoare))
                return culoare, valoare

    @staticmethod
    def reseteaza_carti_folosite():
        Poker.cartiFolosite.clear()

    def carti_jucator(self):
        total_carti_jucator = [Poker.carteMasa1, Poker.carteMasa2, Poker.carteMasa3, Poker.carteMasa4, Poker.carteMasa5,
                               self.carte1, self.carte2]

        for iterator in total_carti_jucator:
            if iterator[1] == 1:
                total_carti_jucator.append((iterator[0], 14))

        return total_carti_jucator

    @staticmethod
    def verifica_chinta_de_culoare(carti):
        vect_frecv_culori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}
        vect_valori = []
        culoare = 0

        for iterator in carti:
            if iterator[0] == "inima" or "romb" or "frunza" or "trefla" and iterator[1] != 14:
                vect_frecv_culori[iterator[0]] += 1

        for (it1, it2) in vect_frecv_culori.items():
            if it2 > 4:
                culoare = it1
        if culoare == 0:
            return None

        for iterator in carti:
            if iterator[0] is culoare:
                vect_valori.append(iterator[1])
        vect_valori.sort()

        for index in range(len(vect_valori) - 1, 3, -1):
            if vect_valori[index - 1] == vect_valori[index] - 1 and \
                    vect_valori[index - 2] == vect_valori[index] - 2 and vect_valori[index - 3] == \
                    vect_valori[index] - 3 and vect_valori[index - 4] == vect_valori[index] - 4:
                return 8, vect_valori[index], "ChintaDeCuloare"

    @staticmethod
    def verifica_careu(carti):
        vect_frecv = [0] * 15

        for iterator in carti:
            vect_frecv[iterator[1]] += 1

        if vect_frecv.count(4):
            return 7, vect_frecv.index(4), "Careu"

    @staticmethod
    def verifica_fullhouse(carti):
        vect_frecv = [0] * 15
        trei = None
        doi = None

        for iterator in carti:
            vect_frecv[iterator[1]] += 1
        vect_frecv[1] = 0

        for i in range(len(vect_frecv) - 1, -1, -1):
            if vect_frecv[i] == 3:
                trei = i
                break
        if trei is None:
            return

        for i in range(len(vect_frecv) - 1, -1, -1):
            if vect_frecv[i] == 2:
                doi = i
                break
        if doi is None:
            return

        return 6, trei, doi, "FullHouse"

    @staticmethod
    def verifica_culoare(carti):
        vect_frecv_culori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}
        vect_max_culori = {"inima": 0, "romb": 0, "frunza": 0, "trefla": 0}

        for iterator in carti:
            if iterator[1] != 14:
                vect_frecv_culori[iterator[0]] += 1
            if iterator[1] > vect_max_culori[iterator[0]]:
                vect_max_culori[iterator[0]] = iterator[1]

        for (it1, it2) in vect_frecv_culori.items():
            if it2 > 4:
                return 5, vect_max_culori[it1], "Culoare"

    @staticmethod
    def verifica_chinta(carti):
        vect_valori = []

        for iterator in carti:
            vect_valori.append(iterator[1])
        vect_valori.sort()

        for index in range(len(vect_valori) - 1, 3, -1):
            if vect_valori[index - 1] == vect_valori[index] - 1 and vect_valori[index - 2] == vect_valori[index] - 2 \
                    and vect_valori[index - 3] == vect_valori[index] - 3 \
                    and vect_valori[index - 4] == vect_valori[index] - 4:
                return 4, vect_valori[index], "Chinta"

    @staticmethod
    def verifica_cui(carti):
        vect_frecv = [0] * 15

        for iterator in carti:
            vect_frecv[iterator[1]] += 1

        for i in range(len(vect_frecv) - 1, 0, -1):
            if vect_frecv[i] == 3:
                return 3, i, "Cui"

    @staticmethod
    def verifica_doua_perechi(carti):
        vect_frecv = [0] * 15
        val1 = None

        for iterator in carti:
            vect_frecv[iterator[1]] += 1
        vect_frecv[1] = 0

        if vect_frecv.count(2) < 2:
            return None

        for i in range(len(vect_frecv) - 1, -1, -1):
            if vect_frecv[i] == 2 and val1 is None:
                val1 = i
            elif vect_frecv[i] == 2:
                if val1 > i:
                    return 2, val1, i, "DouaPerechi"
                else:
                    return 2, i, val1, "DouaPerechi"

    def verifica_pereche(self, carti):
        vect_frecv = [0] * 15

        for iterator in carti:
            vect_frecv[iterator[1]] += 1
        vect_frecv[1] = 0

        if vect_frecv.count(2) > 0:
            vect_frecv.reverse()
            pereche = abs(vect_frecv.index(2) - 14)
            if self.carte1[1] > self.carte2[1]:
                if pereche == self.carte1[1]:
                    kicker = self.carte2[1]
                else:
                    kicker = self.carte1[1]
            else:
                if pereche == self.carte2[1]:
                    kicker = self.carte1[1]
                else:
                    kicker = self.carte2[1]
            if kicker == 1:
                kicker = 14
            return 1, pereche, kicker, "Pereche"

    def verifica_carte_mare(self):
        if self.carte1[1] == 1:
            self.carte1[1] == 14
        if self.carte2[1] == 1:
            self.carte2[1] == 14
        if self.carte1[1] > self.carte2[1]:
            return 0, self.carte1[1], "CarteMare"
        else:
            return 0, self.carte2[1], "CarteMare"

    def mana_maxima(self):

        mana_jucator = self.carti_jucator()
        if Poker.verifica_chinta_de_culoare(mana_jucator):
            return Poker.verifica_chinta_de_culoare(mana_jucator)
        if Poker.verifica_careu(mana_jucator):
            return Poker.verifica_careu(mana_jucator)
        if Poker.verifica_fullhouse(mana_jucator):
            return Poker.verifica_fullhouse(mana_jucator)
        if Poker.verifica_culoare(mana_jucator):
            return Poker.verifica_culoare(mana_jucator)
        if Poker.verifica_chinta(mana_jucator):
            return Poker.verifica_chinta(mana_jucator)
        if Poker.verifica_cui(mana_jucator):
            return Poker.verifica_cui(mana_jucator)
        if Poker.verifica_doua_perechi(mana_jucator):
            return Poker.verifica_doua_perechi(mana_jucator)
        if self.verifica_pereche(mana_jucator):
            return self.verifica_pereche(mana_jucator)
        if self.verifica_carte_mare():
            return self.verifica_carte_mare()

        print("Nu a gasit mana")

    @staticmethod
    def castigator(listaMaini):
        listaCastigatori = []
        listaMainiMaxime = []
        maxim = -1
        for iterator in listaMaini:
            if iterator[0] > maxim:
                maxim = iterator[0]
                listaMainiMaxime.clear()
                listaMainiMaxime.append(iterator)
            elif iterator[0] == maxim:
                listaMainiMaxime.append(iterator)
        if maxim == 0:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)
        elif maxim == 1:
            perecheMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > perecheMaxima:
                    listaCastigatori.clear()
                    listaCastigatori.append(iterator)
                    perecheMaxima = iterator[1]
                elif iterator[1] == perecheMaxima:
                    if iterator[2] > listaCastigatori[0][2]:
                        listaCastigatori.clear()
                        listaCastigatori.append(iterator)
                    elif iterator[2] == listaCastigatori[0][2]:
                        listaCastigatori.append(iterator)
        elif maxim == 2:
            perecheMaxima1 = -1
            perecheMaxima2 = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > perecheMaxima1:
                    listaCastigatori.clear()
                    listaCastigatori.append(iterator)
                    perecheMaxima1 = iterator[1]
                    perecheMaxima2 = iterator[2]
                elif iterator[1] == perecheMaxima1:
                    if iterator[2] > perecheMaxima2:
                        listaCastigatori.clear()
                        listaCastigatori.append(iterator)
                        perecheMaxima2 = iterator[2]
                    elif iterator[2] == perecheMaxima2:
                        listaCastigatori.append(iterator)
        elif maxim == 3:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)
        elif maxim == 4:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)
        elif maxim == 5:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)
        elif maxim == 6:
            perecheMaxima1 = -1
            perecheMaxima2 = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > perecheMaxima1:
                    listaCastigatori.clear()
                    listaCastigatori.append(iterator)
                    perecheMaxima1 = iterator[1]
                    perecheMaxima2 = iterator[2]
                elif iterator[1] == perecheMaxima1:
                    if iterator[2] > perecheMaxima2:
                        listaCastigatori.clear()
                        listaCastigatori.append(iterator)
                        perecheMaxima2 = iterator[2]
                    elif iterator[2] == perecheMaxima2:
                        listaCastigatori.append(iterator)
        elif maxim == 7:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)
        elif maxim == 8:
            carteMaxima = -1
            for iterator in listaMainiMaxime:
                if iterator[1] > carteMaxima:
                    carteMaxima = iterator[1]
            for iterator in listaMainiMaxime:
                if iterator[1] == carteMaxima:
                    listaCastigatori.append(iterator)

        return listaCastigatori


for i in range(1, 100):
    Poker.carteMasa1 = Poker.alege_carte_random()
    Poker.carteMasa2 = Poker.alege_carte_random()
    Poker.carteMasa3 = Poker.alege_carte_random()
    Poker.carteMasa4 = Poker.alege_carte_random()
    Poker.carteMasa5 = Poker.alege_carte_random()

    cul1, val1 = Poker.alege_carte_random()
    cul2, val2 = Poker.alege_carte_random()
    jucator1 = Poker(cul1, val1, cul2, val2)

    cul1, val1 = Poker.alege_carte_random()
    cul2, val2 = Poker.alege_carte_random()
    jucator2 = Poker(cul1, val1, cul2, val2)

    cul1, val1 = Poker.alege_carte_random()
    cul2, val2 = Poker.alege_carte_random()
    jucator3 = Poker(cul1, val1, cul2, val2)

    cul1, val1 = Poker.alege_carte_random()
    cul2, val2 = Poker.alege_carte_random()
    jucator4 = Poker(cul1, val1, cul2, val2)

    j1 = jucator1.mana_maxima()
    j2 = jucator2.mana_maxima()
    j3 = jucator3.mana_maxima()
    j4 = jucator4.mana_maxima()

    listaMainiMaxime = []
    listaMainiMaxime.extend((j1, j2, j3, j4))

    print(f"Carti Masa:{Poker.carteMasa1} {Poker.carteMasa2} {Poker.carteMasa3} {Poker.carteMasa4} {Poker.carteMasa5} \nCarti jucator1: {jucator1.carte1} {jucator1.carte2} \nCarti jucator2: {jucator2.carte1} {jucator2.carte2} \nCarti jucator3: {jucator3.carte1} {jucator3.carte2} \nCarti jucator4: {jucator4.carte1} {jucator4.carte2} \n")
    print(
        f"Mana maxima Jucator1:{j1}\nMana maxima Jucator2:{j2}\nMana maxima Jucator3:{j3}\nMana maxima Jucator4:{j4}\n")

    print("Jucatorii castigatori sunt:", end=' ')
    manaCastigatoare = Poker.castigator(listaMainiMaxime)
    for iterator in manaCastigatoare:
        castigator = listaMainiMaxime.index(iterator)
        listaMainiMaxime.remove(iterator)
        listaMainiMaxime.insert(castigator, -1)
        print(
            f"Jucator{castigator+1} cu mana {iterator},", end=' ')

    print("\n\n")
    Poker.reseteaza_carti_folosite()
