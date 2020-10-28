import chess.pgn
import time
import glob
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import msvcrt
import getch

from matrixManaging import creationDico
from gestionCases import placement, viderCase

os.system('cls')
print("Quelle partie voulez-vous afficher ?")
i = 1

tablo = []

for file in glob.glob("./games/*.pgn"):
    tablo.append(file)
    with open(file) as duel:
        game = chess.pgn.read_game(duel)
    print(i, ":", game.headers["White"], game.headers["WhiteElo"], "vs", game.headers["Black"], game.headers["BlackElo"])
    i+=1

with open(tablo[int(msvcrt.getche())-1]) as duel:
    game = chess.pgn.read_game(duel)

board = game.board()

dictionnaire = creationDico()

pygame.init()
title = game.headers["White"] + " " + game.headers["WhiteElo"] + " vs " + game.headers["Black"] + " " + game.headers["BlackElo"]
pygame.display.set_caption(title)

fenetre = pygame.display.set_mode((600,600))
fond = pygame.image.load("chessBoard600.png").convert()
fenetre.blit(fond, (0,0))

for piece, position in dictionnaire.items():
    screen = placement(fenetre, piece, position)

while(not msvcrt.kbhit()):
    for move in game.mainline_moves():
        pygame.display.flip()
        pygame.event.get()
        strMove = str(move)
        origine, desti = strMove[:len(strMove)//2], strMove[len(strMove)//2:]

        check = 0

        viderCase(screen, origine)

        for piece, position in list(dictionnaire.items()):
            if(desti == dictionnaire[piece]):
                viderCase(screen, desti)
                del dictionnaire[piece]
        for piece, position in dictionnaire.items():
            if(origine == "e8" and desti == "g8" and check == 0):
                placement(fenetre, "bRook2", "f8")
                dictionnaire["bRook2"] = "f8"
                viderCase(screen, "h8")
                check+=1
            if(origine == "e8" and desti == "c8" and check == 0):
                placement(fenetre, "bRook1", "d8")
                dictionnaire["bRook1"] = "d8"
                viderCase(screen, "a8")
                check+=1
            if(origine == "e1" and desti == "g1" and check == 0):
                placement(fenetre, "wRook2", "f1")
                dictionnaire["wRook2"] = "f1"
                viderCase(screen, "h1")
                check+=1
            if(origine == "e1" and desti == "c1" and check == 0):
                placement(fenetre, "wRook1", "d1")
                dictionnaire["wRook1"] = "d1"
                viderCase(screen, "a1")
                check+=1
            if(origine == position):
                placement(fenetre, piece, desti)
                dictionnaire[piece] = desti
        time.sleep(.500)
        board.push(move)

print("fin du jeu")
exit(0)
