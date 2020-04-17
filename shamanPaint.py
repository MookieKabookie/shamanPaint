import pygame, random

pygame.init()

#josh is weak here is my extra line

#new idea--make it so I can introduce as many points as I want and it will self balance where to fill the points in symmetrically

draw = False
oldCoord = (0,0)
oldxFlipCoords = (0,0)
oldyFlipCoords = (0,0)
oldxyFlipCoords = (0,0)
color = (0,0,0)
lineThicc = 3
thickness = 10
if thickness == 10:
    lineThicc = 4
if thickness == 5:
    lineThicc = 2
screenWidth = 1000
screenHeight = 1000

screen = pygame.display.set_mode((screenWidth, screenHeight))

def line (startCoord, endCoord, color, thickness, canvas):
    dx = endCoord[0] - startCoord[0]
    dy = endCoord[1] - startCoord[1]
    longer = max(abs(dx), abs(dy))                                              #here is the def for sweep of circles lines
    for i in range (longer):
        x = int(startCoord[0]+(i/longer)*dx)
        y = int(startCoord[1]+(i/longer)*dy)
        pygame.draw.circle(screen, color, (x,y), thickness)

def xFlipCoord (coord):                                                         #get new coordinates for the reflected lines
    newX = int(screenWidth-coord[0])
    newY = coord[1]
    return (newX, newY)

def yFlipCoord (coord):                                                         #get new coordinates for the reflected lines
    newX = coord[0]
    newY = int(screenHeight-coord[1])
    return (newX, newY)

def xyFlipCoord (coord):                                                         #get new coordinates for the reflected lines
    newX = int(screenWidth-coord[0])
    newY = int(screenHeight-coord[1])
    return (newX, newY)


while True:
    e = pygame.event.wait()
    if e.type == pygame.QUIT:
        pygame.quit()
        break
    if e.type == pygame.MOUSEBUTTONDOWN:
        draw = True
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    if e.type == pygame.MOUSEBUTTONUP:
        draw = False
    if e.type == pygame.MOUSEMOTION:
        if draw == True:
            pygame.draw.circle(screen, color, e.pos, lineThicc)
            line (e.pos, oldCoord, color, thickness, screen)                    #these are both options: this one is my own def using sweep of circles

            xFlipCoords = xFlipCoord (e.pos)
            pygame.draw.circle(screen, color, xFlipCoords, lineThicc)
            line (xFlipCoords, oldxFlipCoords, color, thickness, screen)

            yFlipCoords = yFlipCoord (e.pos)
            pygame.draw.circle(screen, color, yFlipCoords, lineThicc)
            line (yFlipCoords, oldyFlipCoords, color, thickness, screen)

            xyFlipCoords = xyFlipCoord (e.pos)
            pygame.draw.circle(screen, color, xyFlipCoords, lineThicc)
            line (xyFlipCoords, oldxyFlipCoords, color, thickness, screen)


            # pygame.draw.line(screen, color, e.pos, oldCoord, thickness)       #these are both options: this one is pygame provided using rectangles
        oldCoord = e.pos
        oldxFlipCoords = xFlipCoord (e.pos)
        oldyFlipCoords = yFlipCoord (e.pos)
        oldxyFlipCoords = xyFlipCoord (e.pos)
    pygame.display.flip()
