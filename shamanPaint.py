import pygame
import random
import math


shadowClones = 10

screenWidth = 1000
screenHeight = 1000

screen = pygame.display.set_mode((screenWidth, screenHeight))


def line(startCoord, endCoord, color, thickness, canvas):
    dx = int(endCoord[0] - startCoord[0])
    dy = int(endCoord[1] - startCoord[1])
    # here is the def for sweep of circles lines
    longer = max(abs(dx), abs(dy))
    for i in range (int(longer)):
        x = int(startCoord[0] + (i / longer) * dx)
        y = int(startCoord[1] + (i / longer) * dy)
        pygame.draw.circle(screen, color, (x, y), thickness)

def makePolar(coord):
    """
    turn cartesian coords into polar coordinates in degrees
    """
    dx = (coord[0] - screenWidth/2)
    dy = (coord[1] - screenHeight/2)
    if dx == 0:
        rho = int(math.sqrt((dx**2) + (dy**2)))
        theta = 90
        return (rho, theta)
    rho = int(math.sqrt((dx**2) + (dy**2)))
    theta = math.atan(dy / dx)
    return (rho, math.degrees(theta))

def makeCartesian(rho, theta):
    """
    turn polar coordinates in degrees into cartesian
    """
    dx = rho * math.cos(math.radians(theta))
    dy = rho * math.sin(math.radians(theta))
    x = abs(screenWidth / 2 - dx)
    y = abs(screenHeight / 2 - dy)
    return (x,y)

def summonShadowClones(coord, replicas):
    """
    draw all desired shadow summonShadowClones
    """
    thetaBank = []
    cartesianBank = []
    r, t = makePolar(coord)

    if coord[0] > screenWidth / 2:
            t += 180

    # print("before r: ", r, "before t: ", t)
    for i in range(replicas):
        t +=  360/replicas
        # print ("i is: ", i)
        # print(" after r: ", r, "after t: ", t)

        cartesianBank.append(makeCartesian(r, t))

    # print ("cartbank is: ", cartesianBank)
    return (cartesianBank)


def main():

    draw = False
    oldCoord = (420.69, 420.69)
    shadowOld = []
    shadow = []
    color = (0, 0, 0)
    lineThicc = 3
    thickness = 10

    if thickness == 10:
        lineThicc = 4
    if thickness == 5:
        lineThicc = 2

    pygame.init()

    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            pygame.quit()
            break
        elif e.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        elif e.type == pygame.MOUSEBUTTONUP:
            draw = False
        elif e.type == pygame.MOUSEMOTION:
            if draw == True:
                if oldCoord == (420.69, 420.69):
                    continue

                line(e.pos, oldCoord, color, thickness, screen)

                shadow = summonShadowClones(e.pos, shadowClones)

                for i in range(shadowClones):
                    if oldCoord == (420.69, 420.69):
                        continue
                    line(shadow[i], shadowOld[i], color, thickness, screen)


            oldCoord = e.pos
            shadowOld = summonShadowClones(e.pos, shadowClones)

            # for i in range(len(cartesianBank)):

            # shadow1Old = summonShadowClone1(e.pos, shadowClones)


        pygame.display.flip()


if __name__ == '__main__':
    main()
