import pygame
import random
import math

# idea: first line drawn is paintbrush

# idea: animate the lines so they bounce off walls

shadowClones = 50

screenWidth = 1000
screenHeight = 1000

screen = pygame.display.set_mode((screenWidth, screenHeight))

def line(startCoord, endCoord, color, thickness, canvas):
    """
    draw a line
    """
    dx = int(endCoord[0] - startCoord[0])
    dy = int(endCoord[1] - startCoord[1])
    longer = max(abs(dx), abs(dy))
    for i in range (int(longer)):
        x = int(startCoord[0] + (i / longer) * dx)
        y = int(startCoord[1] + (i / longer) * dy)
        pygame.draw.circle(screen, color, (x, y), 0) #"lag" - evan
        # for i in range (thickness):
        #     pygame.draw.circle(screen, color, (x + i, y + i), 0)#caligraphy pen
        #     pygame.draw.circle(screen, color, (x - i, y - i), 0)

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
    draw all desired shadow Clones
    """
    thetaBank = []
    cartesianBank = []
    r, t = makePolar(coord)

    if coord[0] > screenWidth / 2:
        #should this be >=??? is this causing the flip problem
            t += 180
    for i in range(replicas):
        t +=  360/replicas
        cartesianBank.append(makeCartesian(r, t))
    return (cartesianBank)


def main():

    draw = False
    shadowOld = []
    shadow = []
    color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    colorF = (0, 0, 0)
    oldCoord = (0,0,0)
    thickness = 5


    pygame.init()

    while True:
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            pygame.quit()
            break
        # elif e.type == pygame.MOUSERIGHTCLICK:
        #     color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        elif e.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            random255 = random.randint(-100,100)
            colorF = color
            color = (max(min(max(random255 +random.randint(-10,10) + colorF[0],0), 255),0), max(min(max(random255+random.randint(-20,20) + colorF[1],0), 255),0), max(min(max(random255+random.randint(-10,2) + colorF[2],0), 255),0))

            # color = (255,255,255)
        elif e.type == pygame.MOUSEBUTTONUP:
            draw = False
        elif e.type == pygame.MOUSEMOTION:
            if draw == True:

                line(e.pos, oldCoord, color, thickness, screen)

                shadow = summonShadowClones(e.pos, shadowClones)

                for i in range(shadowClones):
                    line(shadow[i], shadowOld[i], color, thickness, screen)

            oldCoord = e.pos
            shadowOld = summonShadowClones(e.pos, shadowClones)


        pygame.display.flip()


if __name__ == '__main__':
    main()
