import pygame

def placement(screen, piece, position):
    table = {"a": 0, "b": 75, "c": 150, "d": 225, "e":300, "f":375, "g":450, "h":525}

    piece = pygame.image.load("./pieces/" + piece[:-1] + ".png").convert_alpha()
    piece = pygame.transform.scale(piece, (75, 75))

    X = int(table.get(position[0]))
    Y = (int(position[1])-1)*75

    screen.blit(piece, (X,Y))

    return screen

def viderCase(screen, position):
    table = {"a": 0, "b": 75, "c": 150, "d": 225, "e":300, "f":375, "g":450, "h":525}

    X = int(table.get(position[0]))
    Y = (int(position[1])-1)*75

    if((int(table.get(position[0])) + int(position[1]))%2 == 0):
        pygame.draw.rect(screen,(124, 187, 161),(X,Y,75,75))
    else:
        pygame.draw.rect(screen,(238, 217, 198),(X,Y,75,75))
