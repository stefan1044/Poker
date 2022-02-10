import pickle
import socket
import pygame
from network import Network
from poker import Poker

pygame.init()

width = 1280
height = 1024
font1=pygame.font.SysFont("arial.ttf",75)
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


clinetNumber = 0

carteStanga = []
carteDreapta = []
carteMasa1=[]
carteMasa2=[]
carteMasa3=[]
carteMasa4=[]
carteMasa5=[]

jucator1Stanga=[]
jucator2Stanga=[]
jucator3Stanga=[]
jucator4Stanga=[]
jucator5Stanga=[]
jucator6Stanga=[]

jucator1Dreapta=[]
jucator2Dreapta=[]
jucator3Dreapta=[]
jucator4Dreapta=[]
jucator5Dreapta=[]
jucator6Dreapta=[]


def alege_imagine(carte):
    if len(carte) == 0:
        imagine=pygame.image.load("COVER.png")
    else:
        imagine=pygame.image.load(str(carte[0])+str(carte[1])+".png")
    return imagine

def redraw_window(win):
    win.fill((50, 200, 100))
    
    
    marimeCarteJucator=100
    imagine1=alege_imagine(jucator1Stanga)
    imagine3=alege_imagine(jucator2Stanga)
    imagine5=alege_imagine(jucator3Stanga)
    imagine7=alege_imagine(jucator4Stanga)
    imagine9=alege_imagine(jucator5Stanga)
    imagine11=alege_imagine(jucator6Stanga)
    imagine2=alege_imagine(jucator1Dreapta)
    imagine4=alege_imagine(jucator2Dreapta)
    imagine6=alege_imagine(jucator3Dreapta)
    imagine8=alege_imagine(jucator4Dreapta)
    imagine10=alege_imagine(jucator5Dreapta)
    imagine12=alege_imagine(jucator6Dreapta)
    imagine1=pygame.transform.scale(imagine1,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine2=pygame.transform.scale(imagine2,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine3=pygame.transform.scale(imagine3,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine4=pygame.transform.scale(imagine4,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine5=pygame.transform.scale(imagine5,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine6=pygame.transform.scale(imagine6,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine7=pygame.transform.scale(imagine7,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine8=pygame.transform.scale(imagine8,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine9=pygame.transform.scale(imagine9,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine10=pygame.transform.scale(imagine10,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine11=pygame.transform.scale(imagine11,(marimeCarteJucator,marimeCarteJucator*1.45))
    imagine12=pygame.transform.scale(imagine12,(marimeCarteJucator,marimeCarteJucator*1.45))
    
    win.blit(imagine1,(60-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine2,(160-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine3,(270-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine4,(370-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine5,(480-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine6,(580-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine7,(690-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine8,(790-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine9,(900-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine10,(1000-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine11,(1110-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))
    win.blit(imagine12,(1210-marimeCarteJucator/2,102-marimeCarteJucator*1.45/2))

    #carti masa
    marimeCarteMasa=150
    imagine1=alege_imagine(carteMasa1)
    imagine2=alege_imagine(carteMasa2)
    imagine3=alege_imagine(carteMasa3)
    imagine4=alege_imagine(carteMasa4)
    imagine5=alege_imagine(carteMasa5)
    imagine1=pygame.transform.scale(imagine1,(marimeCarteMasa,marimeCarteMasa*1.45))
    imagine2=pygame.transform.scale(imagine2,(marimeCarteMasa,marimeCarteMasa*1.45))
    imagine3=pygame.transform.scale(imagine3,(marimeCarteMasa,marimeCarteMasa*1.45))
    imagine4=pygame.transform.scale(imagine4,(marimeCarteMasa,marimeCarteMasa*1.45))
    imagine5=pygame.transform.scale(imagine5,(marimeCarteMasa,marimeCarteMasa*1.45))
        
    win.blit(imagine1,(340-marimeCarteMasa/2,512-marimeCarteMasa*1.45/2))
    win.blit(imagine2,(490-marimeCarteMasa/2,512-marimeCarteMasa*1.45/2))
    win.blit(imagine3,(640-marimeCarteMasa/2,512-marimeCarteMasa*1.45/2))
    win.blit(imagine4,(790-marimeCarteMasa/2,512-marimeCarteMasa*1.45/2))
    win.blit(imagine5,(940-marimeCarteMasa/2,512-marimeCarteMasa*1.45/2))
    
    #carti jucator
    marimeCarteMana=200
    imagineStanga=alege_imagine(carteStanga)
    imagineDreapta=alege_imagine(carteDreapta)
    imagineStanga=pygame.transform.scale(imagineStanga,(marimeCarteMana,marimeCarteMana*1.45))
    imagineDreapta= pygame.transform.scale(imagineDreapta,(marimeCarteMana,marimeCarteMana*1.45))
    
    win.blit(imagineStanga,(639-marimeCarteMana,869-marimeCarteMana*1.45/2))
    win.blit(imagineDreapta,(641,869-marimeCarteMana*1.45/2))

    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = n.getPos()
    print(f"start pos {startPos}")
    clock = pygame.time.Clock()

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
    
    cul1, val1 = Poker.alege_carte_random()
    jucator1Stanga.append(cul1)
    jucator1Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator2Stanga.append(cul1)
    jucator2Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator3Stanga.append(cul1)
    jucator3Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator4Stanga.append(cul1)
    jucator4Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator5Stanga.append(cul1)
    jucator5Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator6Stanga.append(cul1)
    jucator6Stanga.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator1Dreapta.append(cul1)
    jucator1Dreapta.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator2Dreapta.append(cul1)
    jucator2Dreapta.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator3Dreapta.append(cul1)
    jucator3Dreapta.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator4Dreapta.append(cul1)
    jucator4Dreapta.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator5Dreapta.append(cul1)
    jucator5Dreapta.append(val1)
    cul1, val1 = Poker.alege_carte_random()
    jucator6Dreapta.append(cul1)
    jucator6Dreapta.append(val1)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_ESCAPE]:
            pygame.quit()
        redraw_window(win)


main()
