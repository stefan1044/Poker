import pickle
import socket
import pygame
from network import Network
from poker import Poker
import random

pygame.init()

width = 1280
height = 1024
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

font1 = pygame.font.SysFont("trebuchetms", 40)
font1Culoare = (0, 0, 0)

clinetNumber = 0
carteStanga = []
carteDreapta = []

carteMasa1 = []
carteMasa2 = []
carteMasa3 = []
carteMasa4 = []
carteMasa5 = []
pot = 0

listaNumeJucatori = ["NULL"]*6
listaCartiJucatori = ["NULL"]*12
listaSumeJucatori = [0]*6

randClient = True
canCheck = True
apasatButon=False


def verifica_buton(x, y):
    if (950 < x < 1150 and 750 < y < 808):
        if canCheck == True:
            return "Check"
        else:
            return "Call"
    elif (950 < x < 1150 and 850 < y < 908):
        return "Fold"
    elif (100 < x < 300 and 750 < y < 808):
        return "Raise"
    global apasatButon
    apasatButon=True


def alege_imagine(carte):
    if len(carte) == 0 or carte == "NULL":
        imagine = pygame.image.load("COVER.png")
    else:
        imagine = pygame.image.load(str(carte[0])+str(carte[1])+".png")
    return imagine


def redraw_window(win):
    win.fill((50, 200, 100))

    # carti jucatori
    marimeCarteJucator = 100
    pozitie = 60
    index = 0
    for nume in listaNumeJucatori:

        if nume != "NULL":
            imagine = alege_imagine(listaCartiJucatori[index])
            imagine = pygame.transform.scale(
                imagine, (marimeCarteJucator, marimeCarteJucator*1.45))
            win.blit(imagine, (pozitie-marimeCarteJucator /
                     2, 102-marimeCarteJucator*1.45/2))
            imagine = alege_imagine(listaCartiJucatori[index+1])
            imagine = pygame.transform.scale(
                imagine, (marimeCarteJucator, marimeCarteJucator*1.45))
            win.blit(imagine, (pozitie+100-marimeCarteJucator /
                     2, 102-marimeCarteJucator*1.45/2))

            imagine = font1.render(nume, True, font1Culoare)
            win.blit(imagine, (pozitie+30-marimeCarteJucator /
                     2, 252-marimeCarteJucator*1.45/2))
            imagine = font1.render(
                str(listaSumeJucatori[index//2])+"$", True, font1Culoare)
            win.blit(imagine, (pozitie+60-marimeCarteJucator /
                     2, 302-marimeCarteJucator*1.45/2))
        index += 2
        pozitie += 210

    # carti masa
    marimeCarteMasa = 150
    imagine1 = alege_imagine(carteMasa1)
    imagine2 = alege_imagine(carteMasa2)
    imagine3 = alege_imagine(carteMasa3)
    imagine4 = alege_imagine(carteMasa4)
    imagine5 = alege_imagine(carteMasa5)
    imagine1 = pygame.transform.scale(
        imagine1, (marimeCarteMasa, marimeCarteMasa*1.45))
    imagine2 = pygame.transform.scale(
        imagine2, (marimeCarteMasa, marimeCarteMasa*1.45))
    imagine3 = pygame.transform.scale(
        imagine3, (marimeCarteMasa, marimeCarteMasa*1.45))
    imagine4 = pygame.transform.scale(
        imagine4, (marimeCarteMasa, marimeCarteMasa*1.45))
    imagine5 = pygame.transform.scale(
        imagine5, (marimeCarteMasa, marimeCarteMasa*1.45))
    win.blit(imagine1, (300-marimeCarteMasa/2, 512-marimeCarteMasa*1.45/2))
    win.blit(imagine2, (460-marimeCarteMasa/2, 512-marimeCarteMasa*1.45/2))
    win.blit(imagine3, (620-marimeCarteMasa/2, 512-marimeCarteMasa*1.45/2))
    win.blit(imagine4, (780-marimeCarteMasa/2, 512-marimeCarteMasa*1.45/2))
    win.blit(imagine5, (940-marimeCarteMasa/2, 512-marimeCarteMasa*1.45/2))

    imagine = font1.render("Miza:", True, font1Culoare)
    win.blit(imagine, (1050, 462))
    imagine = font1.render(str(pot), True, font1Culoare)
    win.blit(imagine, (1050, 512))

    # carti client
    marimeCarteMana = 200
    imagineStanga = alege_imagine(carteStanga)
    imagineDreapta = alege_imagine(carteDreapta)
    imagineStanga = pygame.transform.scale(
        imagineStanga, (marimeCarteMana, marimeCarteMana*1.45))
    imagineDreapta = pygame.transform.scale(
        imagineDreapta, (marimeCarteMana, marimeCarteMana*1.45))
    win.blit(imagineStanga, (639-marimeCarteMana, 869-marimeCarteMana*1.45/2))
    win.blit(imagineDreapta, (641, 869-marimeCarteMana*1.45/2))

    # butoane
    if randClient == False:
        if canCheck == False:
            imagine = pygame.image.load("call_gray.png")
            imagine = pygame.transform.scale(imagine, (200, 58))
            win.blit(imagine, (950, 750))
        else:
            imagine = pygame.image.load("check_gray.png")
            imagine = pygame.transform.scale(imagine, (200, 58))
            win.blit(imagine, (950, 750))
        imagine = pygame.image.load("fold_gray.png")
        imagine = pygame.transform.scale(imagine, (200, 58))
        win.blit(imagine, (950, 850))
        imagine = pygame.image.load("raise_gray.png")
        imagine = pygame.transform.scale(imagine, (200, 58))
        win.blit(imagine, (100, 750))

    else:
        if canCheck == False:
            imagine = pygame.image.load("call.png")
            imagine = pygame.transform.scale(imagine, (200, 58))
            win.blit(imagine, (950, 750))
        else:
            imagine = pygame.image.load("check.png")
            imagine = pygame.transform.scale(imagine, (200, 58))
            win.blit(imagine, (950, 750))
        imagine = pygame.image.load("fold.png")
        imagine = pygame.transform.scale(imagine, (200, 58))
        win.blit(imagine, (950, 850))
        imagine = pygame.image.load("raise.png")
        imagine = pygame.transform.scale(imagine, (200, 58))
        win.blit(imagine, (100, 750))

    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = n.getPos()
    print(f"start pos {startPos}")
    clock = pygame.time.Clock()

    # testing
    for index in range(0, 6):
        listaCartiJucatori.insert(index*2, Poker.alege_carte_random())
        listaCartiJucatori.insert(index*2+1, Poker.alege_carte_random())
    for index in range(0, 6):
        listaNumeJucatori.insert(index, "Jucator " + str(index))

    cul1, val1 = Poker.alege_carte_random()
    carteStanga.append(cul1)
    carteStanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    carteDreapta.append(cul1)
    carteDreapta.append(val1)

    cul1, val1 = Poker.alege_carte_random()
    carteMasa1.append(cul1)
    carteMasa1.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    carteMasa2.append(cul1)
    carteMasa2.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    carteMasa3.append(cul1)
    carteMasa3.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    carteMasa4.append(cul1)
    carteMasa4.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    carteMasa5.append(cul1)
    carteMasa5.append(val1)

    global canCheck
    canCheck = random.randint(0, 1)
    global randClient
    randClient = random.randint(0, 1)
    # testing
    global apasatButon
    
    while run:
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            clock.tick(60)

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                verifica_buton(mousex, mousey)
                if apasatButon==True:
                    apasatButon=False
                    randClient=False
                
                print(mousex, mousey)
                print(verifica_buton(mousex, mousey))
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_ESCAPE]:
            run = False
            pygame.quit()

        redraw_window(win)


main()
