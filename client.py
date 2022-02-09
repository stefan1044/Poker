import pickle
import socket
import pygame
from network import Network
from poker import Poker

width = 1280
height = 1024
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clinetNumber = 0

carteStanga = []
carteDreapta = []


def redraw_window(win):
    win.fill((50, 200, 100))

    if carteStanga[0] == "inima":
        imagineStanga = pygame.image.load("pokerheart.png")
    elif carteStanga[0] == "romb":
        imagineStanga = pygame.image.load("pokerdiamond.png")
    elif carteStanga[0] == "trefla":
        imagineStanga = pygame.image.load("pokerclub.png")
    elif carteStanga[0] == "frunza":
        imagineStanga = pygame.image.load("pokerspade.png")
    
    if carteDreapta[0] == "inima":
        imagineDreapta = pygame.image.load("pokerheart.png")
    elif carteDreapta[0] == "romb":
        imagineDreapta = pygame.image.load("pokerdiamond.png")
    elif carteDreapta[0] == "trefla":
        imagineDreapta = pygame.image.load("pokerclub.png")
    elif carteDreapta[0] == "frunza":
        imagineDreapta = pygame.image.load("pokerspade.png")
        
    imgS=imagineStanga.get_rect()
    imgD=imagineDreapta.get_rect()
    
    imgS1=imgS.move((340,768))
    imgD1=imgD.move((740,768))
    imgS2=imgS.move((440,924))
    imgD2=imgD.move((840,924))
    
    imagineStanga=pygame.transform.scale(imagineStanga,(100,100))
    imagineDreapta= pygame.transform.scale(imagineDreapta,(100,100))
    
    win.blit(imagineStanga,imgS1)
    win.blit(imagineDreapta,imgD1)
    win.blit(imagineStanga,imgS2)
    win.blit(imagineDreapta,imgD2)
    
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = n.getPos()
    print(f"start pos {startPos}")
    clock = pygame.time.Clock()
    carteStanga.append("trefla")
    carteStanga.append(3)
    carteDreapta.append("romb")
    carteDreapta.append(11)

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
