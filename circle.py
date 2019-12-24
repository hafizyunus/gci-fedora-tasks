import pygame
import math

rad1 = 20*int(input('Enter the radius of circle 1:'))
rad2 = 20*int(input('Enter the radius of circle 2:'))
dist = 20*int(input('Enter the distance from each other:'))

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

if rad1 > rad2:
    gameDisplay = pygame.display.set_mode((rad1*3+dist,rad1*3))
    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay, black, (math.ceil((rad1*1.5+(dist/2))-dist/2),math.ceil(rad1*1.5)), rad1, 3)
    pygame.draw.circle(gameDisplay, black, (math.floor((rad1*1.5+(dist/2))+dist/2),math.floor(rad1*1.5)), rad2, 3)
elif rad1 == rad2:
    gameDisplay = pygame.display.set_mode((rad1*3+dist,rad2*3))
    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay, black, (math.ceil((rad1*1.5+(dist/2))-dist/2),math.ceil(rad1*1.5)), rad1, 3)
    pygame.draw.circle(gameDisplay, black, (math.floor((rad1*1.5+(dist/2))+dist/2),math.floor(rad1*1.5)), rad2, 3)
else:
    gameDisplay = pygame.display.set_mode((rad2*3+dist,rad2*3))
    gameDisplay.fill(white)
    pygame.draw.circle(gameDisplay, black, (math.ceil((rad2*1.5+(dist/2))-dist/2),math.ceil(rad2*1.5)), rad1, 3)
    pygame.draw.circle(gameDisplay, black, (math.floor((rad2*1.5+(dist/2))+dist/2),math.floor(rad2*1.5)), rad2, 3)



if dist == 0:
    if rad1 != rad2:
        print('They are concentric')
    else:
        print('They are identical')
elif dist == rad1 + rad2 or rad1 == dist + rad2 or rad2 == dist + rad1:
    print('They are tangent')
elif dist < rad1 + rad2:
    print('Two points of intersection')
else:
    print('No intersection')




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()